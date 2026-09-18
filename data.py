"""NSE universe and Yahoo completed-bar downloader."""
from __future__ import annotations

import io
import time
from collections.abc import Iterable

import pandas as pd
import requests
import yfinance as yf

NSE_EQUITY_LIST = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"


def get_nse_eq_universe() -> pd.DataFrame:
    """Return the official NSE EQ-series universe with normalized symbols."""
    response = requests.get(NSE_EQUITY_LIST, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()
    frame = pd.read_csv(io.BytesIO(response.content), skipinitialspace=True)
    frame.columns = [str(c).strip() for c in frame.columns]
    frame["SYMBOL"] = frame["SYMBOL"].astype(str).str.strip()
    frame["SERIES"] = frame["SERIES"].astype(str).str.strip()
    return frame.loc[frame["SERIES"].eq("EQ")].drop_duplicates("SYMBOL").sort_values("SYMBOL")


def yahoo_ticker(symbol: str) -> str:
    return f"{symbol}.NS"


def download_daily(symbols: Iterable[str], batch_size: int = 100, pause: float = 1.0) -> dict[str, pd.DataFrame]:
    """Download daily OHLCV. Failed/missing symbols remain absent from the result."""
    symbols = list(symbols)
    result: dict[str, pd.DataFrame] = {}
    for start in range(0, len(symbols), batch_size):
        batch = symbols[start:start + batch_size]
        tickers = [yahoo_ticker(s) for s in batch]
        raw = yf.download(
            tickers=tickers,
            period="2y",
            interval="1d",
            auto_adjust=False,
            actions=False,
            group_by="ticker",
            threads=True,
            progress=False,
        )
        if len(batch) == 1:
            raw = pd.concat({tickers[0]: raw}, axis=1)
        for symbol, ticker in zip(batch, tickers, strict=True):
            try:
                frame = raw[ticker].copy()
            except (KeyError, TypeError):
                continue
            frame.columns = [str(c).title() for c in frame.columns]
            needed = ["Open", "High", "Low", "Close", "Volume"]
            if not set(needed).issubset(frame.columns):
                continue
            frame = frame[needed].dropna(subset=["High", "Low", "Close"])
            if not frame.empty:
                result[symbol] = frame.sort_index()
        if start + batch_size < len(symbols):
            time.sleep(max(0.0, pause))
    return result
