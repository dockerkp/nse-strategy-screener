"""Bull put spread.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.7, PDF p. 20, equations (21), (22), (23), (24).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.7 Strategy: Bull put spread This is a vertical spread consisting of a long position in an OTM put option with a strike price K1 , and a short position in another OTM put option with a higher strike price K2 . This is a net credit trade. The trader’s outlook is bullish. This is an income strategy. We have: fT = (K1 − ST )+ − (K2 − ST )+ + C (21) S∗ = K2 − C (22) Pmax = C (23) Lmax = K2 − K1 − C (24)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.7"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.7 Strategy: Bull put spread This is a vertical spread consisting of a long position in an OTM put option with a strike price K1 , and a short position in another OTM put option with a higher strike price K2 . This is a net credit trade. The trader’s outlook is bullish. This is an income strategy. We have: fT = (K1 − ST )+ − (K2 − ST )+ + C (21) S∗ = K2 − C (22) Pmax = C (23) Lmax = K2 − K1 − C (24)"


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
