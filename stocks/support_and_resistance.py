"""Classic daily pivot levels from Chapter 3 of 151 Trading Strategies."""
from __future__ import annotations

import pandas as pd


def classic_pivot(daily: pd.DataFrame) -> dict:
    """Return center, first resistance, and first support from the latest bar."""
    clean = daily.dropna(subset=["High", "Low", "Close"])
    bar = clean.iloc[-1]
    high, low, close = map(float, (bar["High"], bar["Low"], bar["Close"]))
    center = (high + low + close) / 3.0
    return {"pivot_session": clean.index[-1].date().isoformat(), "pivot": center,
            "resistance_1": 2.0 * center - low, "support_1": 2.0 * center - high}



import math
import pandas as pd


def camarilla(daily: pd.DataFrame) -> dict:
    clean = daily.dropna(subset=["High", "Low", "Close"])
    if clean.empty:
        return {"status": "no_completed_bar"}
    bar = clean.iloc[-1]
    high, low, close = map(float, (bar["High"], bar["Low"], bar["Close"]))
    if not all(math.isfinite(v) for v in (high, low, close)) or high < low:
        return {"status": "invalid_bar"}
    out = {"status": "ok", "source_session": clean.index[-1].date().isoformat(),
           "high": high, "low": low, "close": close}
    for level, denominator in enumerate((12, 6, 4, 2), start=1):
        distance = (high - low) * 1.1 / denominator
        out[f"H{level}"], out[f"L{level}"] = close + distance, close - distance
    return out
