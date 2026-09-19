"""Long call condor.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.46, PDF p. 34, equations (206), (207), (208), (209), (210).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.46 Strategy: Long call condor This is a sideways strategy consisting of a long position in an ITM call option with a strike price K1 , a short position in an ITM call option with a higher strike price K2 , a short position in an OTM call option with a strike price K3 , and a long position in an OTM call option with a higher strike price K4 . All strikes are equidistant: K4 − K3 = K3 − K2 = K2 − K1 = κ. This is a relatively low cost net debit trade. The trader’s outlook is neutral. This is a capital gain strategy. We have: fT = (ST − K1 )+ − (ST − K2 )+ − (ST − K3 )+ + (ST − K4 )+ − D (206) S∗up = K4 − D (207) S∗down = K1 + D (208) 34 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur. All Rights Reserved. Pmax = κ − D (209) Lmax = D (210)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.46"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.46 Strategy: Long call condor This is a sideways strategy consisting of a long position in an ITM call option with a strike price K1 , a short position in an ITM call option with a higher strike price K2 , a short position in an OTM call option with a strike price K3 , and a long position in an OTM call option with a higher strike price K4 . All strikes are equidistant: K4 − K3 = K3 − K2 = K2 − K1 = κ. This is a relatively low cost net debit trade. The trader’s outlook is neutral. This is a capital gain strategy. We have: fT = (ST − K1 )+ − (ST − K2 )+ − (ST − K3 )+ + (ST − K4 )+ − D (206) S∗up = K4 − D (207) S∗down = K1 + D (208) 34 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur. All Rights Reserved. Pmax = κ − D (209) Lmax = D (210)"


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
