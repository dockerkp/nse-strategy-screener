"""Low-volatility ranking from §3.4 of 151 Trading Strategies."""
from __future__ import annotations

import numpy as np
import pandas as pd


def annualized_volatility(daily: pd.DataFrame, lookback: int = 60) -> float | None:
    """Return annualized close-to-close volatility over ``lookback`` bars."""
    returns = daily["Close"].pct_change().dropna().tail(lookback)
    if len(returns) < lookback:
        return None
    return float(returns.std(ddof=1) * np.sqrt(252.0))


def low_volatility_decile(volatility: pd.Series, decile: float = 0.1) -> pd.Series:
    """Select the lowest-volatility cross-sectional decile (§3.4).

    Experimental: the book leaves universe construction and rebalance timing open.
    Missing or non-finite observations are never selected.
    """
    if not 0.0 < decile <= 1.0:
        raise ValueError("decile must be in (0, 1]")
    clean = volatility.replace([np.inf, -np.inf], np.nan).dropna()
    selected = clean.rank(method="first", ascending=True) <= max(1, int(np.ceil(len(clean) * decile)))
    return selected.reindex(volatility.index, fill_value=False).astype(bool)
