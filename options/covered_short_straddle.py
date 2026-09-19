"""Covered short straddle.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.32, PDF p. 29, equations (131), (132), (133), (134).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.32 Strategy: Covered short straddle This strategy amounts to augmenting a covered call by writing a put option with the same strike price K and TTM as the sold call option and thereby increasing the income. The trader’s outlook is bullish. We have: fT = ST − S0 − (ST − K)+ − (K − ST )+ + C (131) 1 S∗ = (S0 + K − C) (132) 2 Pmax = K − S0 + C (133) Lmax = S0 + K − C (134)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.32"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.32 Strategy: Covered short straddle This strategy amounts to augmenting a covered call by writing a put option with the same strike price K and TTM as the sold call option and thereby increasing the income. The trader’s outlook is bullish. We have: fT = ST − S0 − (ST − K)+ − (K − ST )+ + C (131) 1 S∗ = (S0 + K − C) (132) 2 Pmax = K − S0 + C (133) Lmax = S0 + K − C (134)"


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
