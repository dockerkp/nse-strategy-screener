"""Short guts.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.27, PDF p. 27, equations (106), (107), (108), (109), (110).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.27 Strategy: Short guts This is a sideways strategy consisting of a short position in an ITM call option with a strike price K1 , and a short position in an ITM put option with a strike price K2 . This is a net credit trade. Since both call and put options are ITM, the initial 23 Otherwise this strategy would generate risk-free profits. 27 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur. All Rights Reserved. credit is higher than in a short straddle position. The flipside is that the risk is also higher. The trader’s outlook is neutral. This is an income strategy. We have:24 fT = −(ST − K1 )+ − (K2 − ST )+ + C (106) S∗up = K1 + C (107) S∗down = K2 − C (108) Pmax = C − (K2 − K1 ) (109) Lmax = unlimited (110)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.27"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.27 Strategy: Short guts This is a sideways strategy consisting of a short position in an ITM call option with a strike price K1 , and a short position in an ITM put option with a strike price K2 . This is a net credit trade. Since both call and put options are ITM, the initial 23 Otherwise this strategy would generate risk-free profits. 27 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur. All Rights Reserved. credit is higher than in a short straddle position. The flipside is that the risk is also higher. The trader’s outlook is neutral. This is an income strategy. We have:24 fT = −(ST − K1 )+ − (K2 − ST )+ + C (106) S∗up = K1 + C (107) S∗down = K2 − C (108) Pmax = C − (K2 − K1 ) (109) Lmax = unlimited (110)"


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
