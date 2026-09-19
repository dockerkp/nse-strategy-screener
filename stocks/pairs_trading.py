"""Experimental pairs trading from §3.8, eqs. 283-291."""
from __future__ import annotations

import numpy as np
import pandas as pd


def select_correlated_pairs(prices: pd.DataFrame, formation_window: int = 60,
                            min_correlation: float = 0.8) -> pd.DataFrame:
    """Rank unique pairs by correlation of log returns in the formation window."""
    returns = np.log(prices.astype(float)).diff().tail(formation_window)
    corr = returns.corr(min_periods=formation_window)
    rows = [(a, b, float(corr.loc[a, b])) for i, a in enumerate(corr.columns)
            for b in corr.columns[i + 1:] if np.isfinite(corr.loc[a, b])
            and corr.loc[a, b] >= min_correlation]
    return pd.DataFrame(rows, columns=["asset_1", "asset_2", "correlation"]).sort_values(
        "correlation", ascending=False, ignore_index=True)


def pair_signal(prices: pd.DataFrame, asset_1: str, asset_2: str,
                formation_window: int = 60, divergence_threshold: float = 2.0) -> dict:
    """Return a dollar-neutral signal from the pair's demeaned log-price residual.

    Signal +1 means long asset_1/short asset_2; -1 means the reverse.
    Experimental/under-specified: §3.8 leaves pair stability, windows, thresholds,
    exits, and execution choices open.
    """
    pair = np.log(prices[[asset_1, asset_2]].astype(float)).dropna().tail(formation_window)
    if len(pair) < formation_window:
        return {"status": "insufficient_history", "signal": 0}
    demeaned = pair - pair.mean()
    spread = demeaned[asset_1] - demeaned[asset_2]
    sigma = float(spread.std(ddof=1))
    zscore = 0.0 if sigma == 0.0 else float((spread.iloc[-1] - spread.mean()) / sigma)
    signal = -1 if zscore >= divergence_threshold else (1 if zscore <= -divergence_threshold else 0)
    return {"status": "ok", "asset_1": asset_1, "asset_2": asset_2,
            "zscore": zscore, "signal": signal,
            "weights": {asset_1: float(signal), asset_2: float(-signal)}}
