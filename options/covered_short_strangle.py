"""Covered short strangle.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.33, PDF p. 29, equations (135), (136), (137).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.33 Strategy: Covered short strangle This strategy amounts to augmenting a covered call by writing an OTM put option with a strike price K 0 and the same TTM as the sold call option (whose strike price is K) and thereby increasing the income. The trader’s outlook is bullish. We have: fT = ST − S0 − (ST − K)+ − (K 0 − ST )+ + C (135) Pmax = K − S0 + C (136) Lmax = S0 + K 0 − C (137) 29 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur. All Rights Reserved.
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.33"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.33 Strategy: Covered short strangle This strategy amounts to augmenting a covered call by writing an OTM put option with a strike price K 0 and the same TTM as the sold call option (whose strike price is K) and thereby increasing the income. The trader’s outlook is bullish. We have: fT = ST − S0 − (ST − K)+ − (K 0 − ST )+ + C (135) Pmax = K − S0 + C (136) Lmax = S0 + K 0 − C (137) 29 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur. All Rights Reserved."


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
