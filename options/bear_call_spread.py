"""Bear call spread.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.8, PDF p. 20, equations (25), (26), (27), (28).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.8 Strategy: Bear call spread This is a vertical spread consisting of a long position in an OTM call option with a strike price K1 , and a short position in another OTM call option with a lower strike price K2 . This is a net credit trade. The trader’s outlook is bearish. This is an income strategy. We have: fT = (ST − K1 )+ − (ST − K2 )+ + C (25) S∗ = K2 + C (26) Pmax = C (27) Lmax = K1 − K2 − C (28)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.8"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.8 Strategy: Bear call spread This is a vertical spread consisting of a long position in an OTM call option with a strike price K1 , and a short position in another OTM call option with a lower strike price K2 . This is a net credit trade. The trader’s outlook is bearish. This is an income strategy. We have: fT = (ST − K1 )+ − (ST − K2 )+ + C (25) S∗ = K2 + C (26) Pmax = C (27) Lmax = K1 − K2 − C (28)"


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
