"""12-1 price momentum from Chapter 3 of 151 Trading Strategies."""
from __future__ import annotations

import pandas as pd


def price_momentum_12_1(daily: pd.DataFrame) -> float | None:
    """Return the 12-month return excluding the most recent month."""
        monthly = daily["Close"].dropna().resample("ME").last()
            if len(monthly) < 13:
                    return None
                        return float(monthly.iloc[-2] / monthly.iloc[-13] - 1.0)
                        