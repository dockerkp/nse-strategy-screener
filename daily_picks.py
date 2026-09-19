"""Composite top-10 morning screen from completed NSE daily bars."""
from __future__ import annotations

import argparse
from pathlib import Path
import numpy as np
import pandas as pd

from data import download_daily, get_nse_eq_universe
from stocks.support_and_resistance import classic_pivot
from stocks.channel import donchian_state
from stocks.low_volatility_anomaly import annualized_volatility
from stocks.two_moving_averages import ma_10_30_state
from stocks.three_moving_averages import ma_3_10_21_state
from stocks.price_momentum import price_momentum_12_1


def percentile(series: pd.Series, ascending: bool = True) -> pd.Series:
    return series.rank(pct=True, ascending=ascending, method="average")


def build_candidates(history: dict[str, pd.DataFrame]) -> pd.DataFrame:
    rows = []
    for symbol, daily in history.items():
        if daily.empty:
            continue
        mom = price_momentum_12_1(daily)
        vol = annualized_volatility(daily)
        if mom is None or vol is None:
            continue
        ma = {**ma_10_30_state(daily), **ma_3_10_21_state(daily)}
        pivot = classic_pivot(daily)
        close = float(daily["Close"].iloc[-1])
        rows.append({
            "symbol": symbol,
            "data_session": daily.index[-1].date().isoformat(),
            "close": close,
            "momentum_12_1": mom,
            "annualized_volatility": vol,
            "donchian_state": donchian_state(daily),
            **ma, **pivot,
        })
    frame = pd.DataFrame(rows)
    if frame.empty:
        return frame
    # Strict freshness: only compare names carrying the modal latest session.
    expected_session = frame["data_session"].mode().iloc[0]
    frame = frame.loc[frame["data_session"].eq(expected_session)].copy()
    frame["momentum_rank"] = percentile(frame["momentum_12_1"])
    frame["low_vol_rank"] = percentile(frame["annualized_volatility"], ascending=False)
    frame["ma_score"] = (frame["ma10_30"] + frame["ma3_10_21"] + 2.0) / 4.0
    frame["donchian_score"] = (frame["donchian_state"] + 1.0) / 2.0
    frame["pivot_opportunity"] = np.where(
        frame["close"] >= frame["pivot"],
        (frame["resistance_1"] - frame["close"]) / frame["close"],
        (frame["close"] - frame["support_1"]) / frame["close"],
    ).clip(lower=0)
    frame["pivot_rank"] = percentile(frame["pivot_opportunity"])
    frame["composite_score"] = (
        0.40 * frame["momentum_rank"] + 0.30 * frame["ma_score"]
        + 0.15 * frame["low_vol_rank"] + 0.10 * frame["pivot_rank"]
        + 0.05 * frame["donchian_score"]
    )
    return frame


def make_top_picks(candidates: pd.DataFrame, count: int = 10) -> pd.DataFrame:
    if candidates.empty:
        return candidates
    picks = candidates.nlargest(count, "composite_score").copy()
    picks["direction"] = np.where(picks["close"] >= picks["pivot"], "LONG", "SHORT")
    # Pivot crossing is the next-session trigger; target uses R1/S1.
    picks["entry_trigger"] = picks["pivot"]
    picks["target"] = np.where(picks["direction"].eq("LONG"), picks["resistance_1"], picks["support_1"])
    picks["stop_loss"] = np.where(
        picks["direction"].eq("LONG"), picks["entry_trigger"] * 0.98, picks["entry_trigger"] * 1.02
    )
    picks["strategies_agree"] = picks.apply(
        lambda r: ", ".join(filter(None, [
            "12-1 momentum" if r.momentum_rank >= 0.9 else "",
            "MA10>MA30" if r.ma10_30 > 0 else "",
            "MA3>MA10>MA21" if r.ma3_10_21 > 0 else "",
            "Donchian breakout" if r.donchian_state > 0 else "",
            "low volatility" if r.low_vol_rank >= 0.7 else "",
        ])), axis=1,
    )
    columns = [
        "symbol", "data_session", "direction", "entry_trigger", "target", "stop_loss",
        "composite_score", "strategies_agree", "close", "pivot", "resistance_1", "support_1",
        "momentum_12_1", "annualized_volatility",
    ]
    return picks[columns]


def main() -> None:
    parser = argparse.ArgumentParser(description="Composite daily NSE top-10 screen")
    parser.add_argument("--output", default="output/daily_top10.csv")
    parser.add_argument("--batch-size", type=int, default=100)
    parser.add_argument("--pause", type=float, default=1.0)
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()
    symbols = get_nse_eq_universe()["SYMBOL"].tolist()
    if args.limit:
        symbols = symbols[:args.limit]
    history = download_daily(symbols, batch_size=args.batch_size, pause=args.pause)
    candidates = build_candidates(history)
    picks = make_top_picks(candidates)
    destination = Path(args.output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    picks.to_csv(destination, index=False, float_format="%.4f")
    print(picks.to_string(index=False))
    print(f"\nEligible current-session symbols: {len(candidates)} / {len(symbols)}")
    print(f"Saved: {destination.resolve()}")


if __name__ == "__main__":
    main()
