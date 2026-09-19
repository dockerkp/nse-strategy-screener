"""Short straddle.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.25, PDF p. 27, equations (96), (97), (98), (99), (100).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.25 Strategy: Short straddle This a is sideways strategy consisting of a short position in an ATM call option, and a short position in an ATM put option with a strike price K. This is a net credit trade. The trader’s outlook is neutral. This is an income strategy. We have: fT = −(ST − K)+ − (K − ST )+ + C (96) S∗up = K + C (97) S∗down = K − C (98) Pmax = C (99) Lmax = unlimited (100)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.25"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.25 Strategy: Short straddle This a is sideways strategy consisting of a short position in an ATM call option, and a short position in an ATM put option with a strike price K. This is a net credit trade. The trader’s outlook is neutral. This is an income strategy. We have: fT = −(ST − K)+ − (K − ST )+ + C (96) S∗up = K + C (97) S∗down = K − C (98) Pmax = C (99) Lmax = unlimited (100)"


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
