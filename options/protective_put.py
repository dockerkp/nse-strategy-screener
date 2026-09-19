"""Protective put.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.4, PDF p. 19, equations (9), (10), (11), (12).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.4 Strategy: Protective put This strategy (a.k.a. “married put” or “synthetic call”) amounts to buying stock and an ATM or OTM put option with a strike price K ≤ S0 . The trader’s outlook is bullish. This is a hedging strategy: the put option hedges the risk of the stock price falling. We have:13 fT = ST − S0 + (K − ST )+ − D = K − S0 + (ST − K)+ − D (9) S∗ = S0 + D (10) Pmax = unlimited (11) Lmax = S0 − K + D (12)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.4"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.4 Strategy: Protective put This strategy (a.k.a. “married put” or “synthetic call”) amounts to buying stock and an ATM or OTM put option with a strike price K ≤ S0 . The trader’s outlook is bullish. This is a hedging strategy: the put option hedges the risk of the stock price falling. We have:13 fT = ST − S0 + (K − ST )+ − D = K − S0 + (ST − K)+ − D (9) S∗ = S0 + D (10) Pmax = unlimited (11) Lmax = S0 − K + D (12)"


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
