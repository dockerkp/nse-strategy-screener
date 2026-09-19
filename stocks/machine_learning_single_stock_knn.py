"""Experimental single-stock KNN from §3.17, eqs. 332-341."""
from __future__ import annotations

import numpy as np
import pandas as pd


def single_stock_knn(daily: pd.DataFrame, price_windows: tuple[int, ...] = (5, 10, 20),
                     volume_windows: tuple[int, ...] = (5, 10, 20), k: int = 5,
                     forward_horizon: int = 5, z1: float = 0.01,
                     z2: float = 0.0) -> dict:
    """Predict forward return from normalized MA-of-price/volume feature neighbors.

    ``z1`` is the entry magnitude and ``z2`` the exit band: prediction above z1
    is long, below -z1 is short, and within +/-z2 is exit/flat.
    Experimental/under-specified: §3.17 leaves windows, k, distance treatment,
    thresholds, and validation protocol open, so tune out of sample.
    """
    if k < 1 or forward_horizon < 1 or z1 < z2 or z2 < 0:
        raise ValueError("require k >= 1, horizon >= 1, and z1 >= z2 >= 0")
    clean = daily[["Close", "Volume"]].astype(float).replace([np.inf, -np.inf], np.nan)
    features = {}
    for window in price_windows:
        features[f"price_ma_{window}"] = clean["Close"].rolling(window).mean() / clean["Close"]
    for window in volume_windows:
        features[f"volume_ma_{window}"] = clean["Volume"].rolling(window).mean() / clean["Volume"].replace(0, np.nan)
    x = pd.DataFrame(features, index=clean.index)
    future = clean["Close"].shift(-forward_horizon) / clean["Close"] - 1.0
    valid_x = x.dropna()
    if valid_x.empty:
        return {"status": "insufficient_history", "signal": 0}
    current = valid_x.iloc[-1]
    historical = x.loc[:valid_x.index[-1]].iloc[:-forward_horizon].copy()
    training = historical.join(future.rename("target")).dropna()
    if len(training) < k:
        return {"status": "insufficient_history", "signal": 0}
    all_x = pd.concat([training[x.columns], current.to_frame().T])
    span = (all_x.max() - all_x.min()).replace(0.0, 1.0)
    normalized = (all_x - all_x.min()) / span
    current_n = normalized.iloc[-1]
    distances = ((normalized.iloc[:-1] - current_n) ** 2).sum(axis=1).pow(0.5)
    neighbors = distances.nsmallest(k).index
    prediction = float(training.loc[neighbors, "target"].mean())
    signal = 1 if prediction >= z1 else (-1 if prediction <= -z1 else 0)
    if abs(prediction) <= z2:
        signal = 0
    return {"status": "ok", "prediction": prediction, "signal": signal,
            "neighbors": list(neighbors), "k": k}
