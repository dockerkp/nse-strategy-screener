"""Strip.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.35, PDF p. 30, equations (143), (144), (145), (146), (147).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.35 Strategy: Strip This is a volatility strategy consisting of a long position in an ATM call option, and a long position in two ATM put options with a strike price K. This is a net debit trade. The trader’s outlook is bearish. This is a capital gain strategy. We have: fT = (ST − K)+ + 2 × (K − ST )+ − D (143) S∗up = K + D (144) D S∗down = K − (145) 2 Pmax = unlimited (146) Lmax = D (147)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.35"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.35 Strategy: Strip This is a volatility strategy consisting of a long position in an ATM call option, and a long position in two ATM put options with a strike price K. This is a net debit trade. The trader’s outlook is bearish. This is a capital gain strategy. We have: fT = (ST − K)+ + 2 × (K − ST )+ − D (143) S∗up = K + D (144) D S∗down = K − (145) 2 Pmax = unlimited (146) Lmax = D (147)"


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
