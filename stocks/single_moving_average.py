"""Single moving average.

Source: Kakushadze & Serur, 151 Trading Strategies, §3.11, PDF p. 49, equations (319), (320), (321).
Status: RUNNABLE_NSE_DAILY_OHLCV.
Data requirements: completed stock OHLCV plus any fundamentals, events, sectors or options explicitly named by the rule.

Book rule summary: 3.11 Strategy: Single moving average This strategy is based on the stock price crossing a moving average. One can use different types of moving averages (MAs), such as a simple moving average (SMA), 54 For some literature on mean-reversion (a.k.a. contrarian) strategies, see, e.g., [Avellaneda and Lee, 2010], [Black and Litterman, 1991], [Black and Litterman, 1992], [Cheung, 2010], [Chin, Prevost and Gottesman, 2002], [Conrad and Kaul, 1998], [Daniel, 2001], [Da Silva, Lee and Porn- rojnangkool, 2009], [Doan, Alexeev and Brooks, 2014], [Drobetz, 2001], [Hodges and Carverhill, 1993], [Idzorek, 2007], [Jansen and Nikiforov, 2016], [Jegadeesh and Titman, 1995], [Kakushadze, 2015b], [Kang, Liu and Ni, 2002], [Kudryavtsev, 2012], [Lakonishok, Shleifer and Vishny, 1994], [Lehmann, 1990], [Li et al, 2012], [Liew and Roberts, 2013], [Lo and MacKinlay, 1990], [Mun, Vas- concellos and Kish,
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "3.11"
STATUS = "RUNNABLE_NSE_DAILY_OHLCV"
DATA_REQUIREMENTS = "completed stock OHLCV plus any fundamentals, events, sectors or options explicitly named by the rule"
SIGNAL_RULE = "3.11 Strategy: Single moving average This strategy is based on the stock price crossing a moving average. One can use different types of moving averages (MAs), such as a simple moving average (SMA), 54 For some literature on mean-reversion (a.k.a. contrarian) strategies, see, e.g., [Avellaneda and Lee, 2010], [Black and Litterman, 1991], [Black and Litterman, 1992], [Cheung, 2010], [Chin, Prevost and Gottesman, 2002], [Conrad and Kaul, 1998], [Daniel, 2001], [Da Silva, Lee and Porn- rojnangkool, 2009], [Doan, Alexeev and Brooks, 2014], [Drobetz, 2001], [Hodges and Carverhill, 1993], [Idzorek, 2007], [Jansen and Nikiforov, 2016], [Jegadeesh and Titman, 1995], [Kakushadze, 2015b], [Kang, Liu and Ni, 2002], [Kudryavtsev, 2012], [Lakonishok, Shleifer and Vishny, 1994], [Lehmann, 1990], [Li et al, 2012], [Liew and Roberts, 2013], [Lo and MacKinlay, 1990], [Mun, Vas- concellos and Kish,"


def signal(inputs: Mapping[str, Any]) -> dict[str, Any]:
    """Return an explicit strategy instruction after checking supplied inputs.

    Reference-only modules do not fabricate unavailable market data or execution.
    Their output preserves the cited rule and reports whether the caller supplied
    data, so a future feed adapter can implement the trade without changing the API.
    """
    return {
        "section": SECTION,
        "status": STATUS,
        "ready": bool(inputs),
        "data_requirements": DATA_REQUIREMENTS,
        "rule": SIGNAL_RULE,
        "inputs": dict(inputs),
    }



import pandas as pd


def screen_above_52_week_sma(daily: pd.DataFrame) -> dict:
    close = daily["Close"].dropna()
    weekly = close.resample("W-FRI").last().dropna()
    if len(weekly) < 52:
        return {"status": "insufficient_weekly_history", "weekly_closes": len(weekly)}
    latest_close, sma_52w = float(close.iloc[-1]), float(weekly.iloc[-52:].mean())
    return {"status": "ok", "weekly_closes": len(weekly),
            "price_date": close.index[-1].date().isoformat(), "latest_close": latest_close,
            "sma_52w": sma_52w, "pct_above_sma": (latest_close / sma_52w - 1.0) * 100.0,
            "passes": bool(latest_close > sma_52w)}
