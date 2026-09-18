"""Trend screen and daily Camarilla levels using completed OHLCV bars."""
from __future__ import annotations

import math
import pandas as pd


def screen_above_52_week_sma(daily: pd.DataFrame) -> dict:
    close = daily["Close"].dropna()
    weekly = close.resample("W-FRI").last().dropna()
    if len(weekly) < 52:
        return {"status": "insufficient_weekly_history", "weekly_closes": len(weekly)}
    latest_close = float(close.iloc[-1])
    sma_52w = float(weekly.iloc[-52:].mean())
    return {
        "status": "ok",
        "weekly_closes": len(weekly),
        "price_date": close.index[-1].date().isoformat(),
        "latest_close": latest_close,
        "sma_52w": sma_52w,
        "pct_above_sma": (latest_close / sma_52w - 1.0) * 100.0,
        "passes": bool(latest_close > sma_52w),
    }


def camarilla(daily: pd.DataFrame) -> dict:
    clean = daily.dropna(subset=["High", "Low", "Close"])
    if clean.empty:
        return {"status": "no_completed_bar"}
    bar = clean.iloc[-1]
    high, low, close = map(float, (bar["High"], bar["Low"], bar["Close"]))
    if not all(math.isfinite(v) for v in (high, low, close)) or high < low:
        return {"status": "invalid_bar"}
    r = high - low
    out = {
        "status": "ok",
        "source_session": clean.index[-1].date().isoformat(),
        "high": high,
        "low": low,
        "close": close,
    }
    for level, denominator in enumerate((12, 6, 4, 2), start=1):
        distance = r * 1.1 / denominator
        out[f"H{level}"] = close + distance
        out[f"L{level}"] = close - distance
    return out
