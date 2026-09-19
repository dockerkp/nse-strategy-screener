"""Short iron condor.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.51, PDF p. 36, equations (231), (232), (233), (234), (235).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.51 Strategy: Short iron condor This volatility strategy is a combination of a bear put spread and a bull call spread and consists of a short position in an OTM put option with a strike price K1 , a long position in an OTM put option with a higher strike price K2 , a long position in an OTM call option with a strike price K3 , and a short position in an OTM call option with a higher strike price K4 . The strikes are equidistant: K4 − K3 = K3 − K2 = K2 − K1 = κ. This is a net debit trade. The trader’s outlook is neutral. This is a capital gain strategy. We have: fT = (K2 − ST )+ + (ST − K3 )+ − (K1 − ST )+ − (ST − K4 )+ − D (231) S∗up = K3 + D (232) S∗down = K2 − D (233) Pmax = κ − D (234) Lmax = D (235) 36 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur. All Rights Reserved.
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.51"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.51 Strategy: Short iron condor This volatility strategy is a combination of a bear put spread and a bull call spread and consists of a short position in an OTM put option with a strike price K1 , a long position in an OTM put option with a higher strike price K2 , a long position in an OTM call option with a strike price K3 , and a short position in an OTM call option with a higher strike price K4 . The strikes are equidistant: K4 − K3 = K3 − K2 = K2 − K1 = κ. This is a net debit trade. The trader’s outlook is neutral. This is a capital gain strategy. We have: fT = (K2 − ST )+ + (ST − K3 )+ − (K1 − ST )+ − (ST − K4 )+ − D (231) S∗up = K3 + D (232) S∗down = K2 − D (233) Pmax = κ − D (234) Lmax = D (235) 36 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur. All Rights Reserved."


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
