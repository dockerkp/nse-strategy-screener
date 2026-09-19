"""3/10/21 moving-average alignment from Chapter 3 of 151 Trading Strategies."""
from __future__ import annotations

import pandas as pd


def ma_3_10_21_state(daily: pd.DataFrame) -> dict:
    """Return averages and aligned trend state (+1, -1, or 0)."""
    close = daily["Close"].dropna()
    if len(close) < 21:
        return {"ma3_10_21": 0}
    ma3, ma10, ma21 = (float(close.tail(n).mean()) for n in (3, 10, 21))
    state = 1 if ma3 > ma10 > ma21 else (-1 if ma3 < ma10 < ma21 else 0)
    return {"ma3": ma3, "ma10": ma10, "ma21": ma21, "ma3_10_21": state}
