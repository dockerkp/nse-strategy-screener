"""10/30 moving-average state from Chapter 3 of 151 Trading Strategies."""
from __future__ import annotations

import pandas as pd


def ma_10_30_state(daily: pd.DataFrame) -> dict:
    """Return moving averages and +1/-1 state; 0 means insufficient history."""
    close = daily["Close"].dropna()
    if len(close) < 30:
        return {"ma10_30": 0}
    ma10, ma30 = (float(close.tail(n).mean()) for n in (10, 30))
    return {"ma10": ma10, "ma30": ma30, "ma10_30": 1 if ma10 > ma30 else -1}
