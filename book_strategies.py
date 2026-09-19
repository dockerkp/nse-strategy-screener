"""Daily-bar strategies adapted from Chapter 3 of 151 Trading Strategies.

The book generally defines signals, not exact executable prices or stops. The
2% stop used by the composite engine is the explicit example from its two-MA
section and is applied as a common risk overlay.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def price_momentum_12_1(daily: pd.DataFrame) -> float | None:
    """12-month return skipping the most recent month, from adjusted daily closes."""
    monthly = daily["Close"].dropna().resample("ME").last()
    if len(monthly) < 13:
        return None
    return float(monthly.iloc[-2] / monthly.iloc[-13] - 1.0)


def moving_average_state(daily: pd.DataFrame) -> dict:
    close = daily["Close"].dropna()
    if len(close) < 30:
        return {"ma10_30": 0, "ma3_10_21": 0}
    ma3, ma10, ma21, ma30 = (float(close.tail(n).mean()) for n in (3, 10, 21, 30))
    return {
        "ma3": ma3, "ma10": ma10, "ma21": ma21, "ma30": ma30,
        "ma10_30": 1 if ma10 > ma30 else -1,
        "ma3_10_21": 1 if ma3 > ma10 > ma21 else (-1 if ma3 < ma10 < ma21 else 0),
    }


def classic_pivot(daily: pd.DataFrame) -> dict:
    """Classic pivot C, first resistance R and first support S from latest completed bar."""
    bar = daily.dropna(subset=["High", "Low", "Close"]).iloc[-1]
    high, low, close = map(float, (bar["High"], bar["Low"], bar["Close"]))
    center = (high + low + close) / 3.0
    return {
        "pivot_session": daily.dropna(subset=["High", "Low", "Close"]).index[-1].date().isoformat(),
        "pivot": center,
        "resistance_1": 2.0 * center - low,
        "support_1": 2.0 * center - high,
    }


def annualized_volatility(daily: pd.DataFrame, lookback: int = 60) -> float | None:
    returns = daily["Close"].pct_change().dropna().tail(lookback)
    if len(returns) < lookback:
        return None
    return float(returns.std(ddof=1) * np.sqrt(252.0))


def donchian_state(daily: pd.DataFrame, lookback: int = 20) -> int:
    """Supporting state: +1 above prior channel high, -1 below prior channel low."""
    if len(daily) < lookback + 1:
        return 0
    current = float(daily["Close"].iloc[-1])
    prior = daily.iloc[-lookback - 1:-1]
    if current > float(prior["High"].max()):
        return 1
    if current < float(prior["Low"].min()):
        return -1
    return 0
