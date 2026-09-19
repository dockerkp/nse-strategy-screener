"""Long call butterfly.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.40, PDF p. 32, equations (168), (169), (170), (171), (172).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.40 Strategy: Long call butterfly This is a sideways strategy consisting of a long position in an OTM call option with a strike price K1 , a short position in two ATM call options with a strike price K2 , and a long position in an ITM call option with a strike price K3 . The strikes are equidistant: K2 − K3 = K1 − K2 = κ. This is a relatively low cost net debit trade. The trader’s outlook is neutral. This is a capital gain strategy. We have:29 fT = (ST − K1 )+ + (ST − K3 )+ − 2 × (ST − K2 )+ − D (168) S∗down = K3 + D (169) S∗up = K1 − D (170) Pmax = κ − D (171) Lmax = D (172)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.40"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.40 Strategy: Long call butterfly This is a sideways strategy consisting of a long position in an OTM call option with a strike price K1 , a short position in two ATM call options with a strike price K2 , and a long position in an ITM call option with a strike price K3 . The strikes are equidistant: K2 − K3 = K1 − K2 = κ. This is a relatively low cost net debit trade. The trader’s outlook is neutral. This is a capital gain strategy. We have:29 fT = (ST − K1 )+ + (ST − K3 )+ − 2 × (ST − K2 )+ − D (168) S∗down = K3 + D (169) S∗up = K1 − D (170) Pmax = κ − D (171) Lmax = D (172)"


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
