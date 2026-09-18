from __future__ import annotations

import argparse
from pathlib import Path
import pandas as pd

from data import download_daily, get_nse_eq_universe
from trend_and_levels import camarilla, screen_above_52_week_sma


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Strict NSE 52-week SMA and daily Camarilla screen")
    parser.add_argument("--output-dir", default="output")
    parser.add_argument("--batch-size", type=int, default=100)
    parser.add_argument("--pause", type=float, default=1.0)
    parser.add_argument("--limit", type=int, help="Limit symbols for a quick test")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    universe = get_nse_eq_universe()
    if args.limit:
        universe = universe.head(args.limit)
    symbols = universe["SYMBOL"].tolist()
    history = download_daily(symbols, batch_size=args.batch_size, pause=args.pause)

    coverage, passed, levels = [], [], []
    for symbol in symbols:
        daily = history.get(symbol)
        if daily is None or daily.empty:
            coverage.append({"symbol": symbol, "status": "no_yahoo_history"})
            continue
        sma = screen_above_52_week_sma(daily)
        coverage.append({"symbol": symbol, **sma})
        if sma.get("status") == "ok" and sma.get("passes"):
            passed.append({"symbol": symbol, **sma})
            levels.append({"symbol": symbol, **camarilla(daily)})

    pd.DataFrame(passed).sort_values("pct_above_sma", ascending=False).to_csv(
        output_dir / "nse_52week_sma_screen.csv", index=False, float_format="%.4f"
    )
    pd.DataFrame(levels).to_csv(
        output_dir / "nse_daily_camarilla.csv", index=False, float_format="%.4f"
    )
    pd.DataFrame(coverage).to_csv(output_dir / "coverage_report.csv", index=False, float_format="%.4f")
    print(f"Universe: {len(symbols)} | Downloaded: {len(history)} | Above SMA: {len(passed)}")
    print(f"Output: {output_dir.resolve()}")


if __name__ == "__main__":
    main()
