"""Experimental mean-reversion residuals from §§3.9-3.10, eqs. 292-318."""
from __future__ import annotations

import numpy as np
import pandas as pd


def _log_returns(prices: pd.DataFrame) -> pd.DataFrame:
    return np.log(prices.astype(float)).diff()


def single_cluster_mean_reversion(prices: pd.DataFrame, lookback: int = 20,
                                  threshold: float = 1.0) -> pd.DataFrame:
    """Signal demeaned stock returns against one cluster mean.

    Returns residual, z-score, and contrarian signal (-sign(z) beyond threshold).
    Experimental/under-specified: §§3.9-3.10 do not fix cluster membership,
    lookback, threshold, weighting, or trading costs.
    """
    if lookback < 2 or threshold < 0:
        raise ValueError("lookback must be >= 2 and threshold must be non-negative")
    returns = _log_returns(prices)
    residuals = returns.sub(returns.mean(axis=1), axis=0)
    window = residuals.tail(lookback)
    latest = window.iloc[-1]
    scale = window.std(ddof=1).replace(0.0, np.nan)
    zscore = latest.sub(window.mean()).div(scale)
    signal = -np.sign(zscore).where(zscore.abs() >= threshold, 0.0).fillna(0.0)
    return pd.DataFrame({"residual": latest, "zscore": zscore, "signal": signal.astype(int)})


def multi_cluster_mean_reversion(prices: pd.DataFrame, clusters: pd.Series,
                                 lookback: int = 20, threshold: float = 1.0) -> pd.DataFrame:
    """Signal residuals against each stock's cluster/sector mean (eqs. 292-318).

    ``clusters`` maps price columns to labels. Experimental/under-specified for
    the same parameter and execution choices as ``single_cluster_mean_reversion``.
    """
    missing = prices.columns.difference(clusters.index)
    if len(missing):
        raise ValueError(f"missing cluster labels: {list(missing)}")
    returns = _log_returns(prices)
    residuals = returns.copy()
    for label in clusters.loc[prices.columns].unique():
        members = clusters.index[clusters.eq(label)].intersection(prices.columns)
        residuals.loc[:, members] = returns[members].sub(returns[members].mean(axis=1), axis=0)
    window = residuals.tail(lookback)
    latest = window.iloc[-1]
    zscore = latest.sub(window.mean()).div(window.std(ddof=1).replace(0.0, np.nan))
    signal = -np.sign(zscore).where(zscore.abs() >= threshold, 0.0).fillna(0.0)
    return pd.DataFrame({"residual": latest, "zscore": zscore, "signal": signal.astype(int),
                         "cluster": clusters.loc[prices.columns]})
