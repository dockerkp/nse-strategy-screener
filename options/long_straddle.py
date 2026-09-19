"""Long straddle.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.22, PDF p. 26, equations (81), (82), (83), (84), (85).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.22 Strategy: Long straddle This is a volatility strategy consisting of a long position in an ATM call option, and a long position in an ATM put option with a strike price K. This is a net debit trade. The trader’s outlook is neutral. This is a capital gain strategy. We have22 : fT = (ST − K)+ + (K − ST )+ − D (81) S∗up = K + D (82) S∗down = K − D (83) Pmax = unlimited (84) Lmax = D (85)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.22"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.22 Strategy: Long straddle This is a volatility strategy consisting of a long position in an ATM call option, and a long position in an ATM put option with a strike price K. This is a net debit trade. The trader’s outlook is neutral. This is a capital gain strategy. We have22 : fT = (ST − K)+ + (K − ST )+ − D (81) S∗up = K + D (82) S∗down = K − D (83) Pmax = unlimited (84) Lmax = D (85)"


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
