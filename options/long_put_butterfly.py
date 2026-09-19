"""Long put butterfly.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.41, PDF p. 32, equations (177), (178), (179), (180), (181).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.41 Strategy: Long put butterfly This is a sideways strategy consisting of a long position in an OTM put option with a strike price K1 , a short position in two ATM put options with a strike price K2 , and a long position in an ITM put option with a strike price K3 . The strikes are equidistant: K3 − K2 = K2 − K1 = κ. This is a relatively low cost net debit trade. The trader’s outlook is neutral. This is a capital gain strategy. We have: fT = (K1 − ST )+ + (K3 − ST )+ − 2 × (K2 − ST )+ − D (177) S∗up = K3 − D (178) S∗down = K1 + D (179) Pmax = κ − D (180) Lmax = D (181) 29 For some literature on butterfly spreads (including iron butterflies), see, e.g., [Balbás, Lon- garela and Lucia, 1999], [Howison, Reisinger and Witte, 2013], [Jongadsayakul, 2017], [Matsypura and Timkovsky, 2010], [Youbi, Pindza and Maré, 2017], [Wolf, 2014], [Wystup, 2017]. Academic literature on condor
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.41"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.41 Strategy: Long put butterfly This is a sideways strategy consisting of a long position in an OTM put option with a strike price K1 , a short position in two ATM put options with a strike price K2 , and a long position in an ITM put option with a strike price K3 . The strikes are equidistant: K3 − K2 = K2 − K1 = κ. This is a relatively low cost net debit trade. The trader’s outlook is neutral. This is a capital gain strategy. We have: fT = (K1 − ST )+ + (K3 − ST )+ − 2 × (K2 − ST )+ − D (177) S∗up = K3 − D (178) S∗down = K1 + D (179) Pmax = κ − D (180) Lmax = D (181) 29 For some literature on butterfly spreads (including iron butterflies), see, e.g., [Balbás, Lon- garela and Lucia, 1999], [Howison, Reisinger and Witte, 2013], [Jongadsayakul, 2017], [Matsypura and Timkovsky, 2010], [Youbi, Pindza and Maré, 2017], [Wolf, 2014], [Wystup, 2017]. Academic literature on condor"


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
