"""Short put butterfly.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.43, PDF p. 33, equations (191), (192), (193), (194), (195).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.43 Strategy: Short put butterfly This is a volatility strategy consisting of a short position in an ITM put option with a strike price K1 , a long position in two ATM put options with a strike price K2 , and a short position in an OTM put option with a strike price K3 . The strikes are equidistant: K2 − K3 = K1 − K2 = κ. This is a net credit trade. In this sense, this is an income strategy. However, the potential reward is sizably smaller than with a short straddle or a short strangle (albeit with a lower risk). The trader’s outlook is neutral. We have: fT = 2 × (K2 − ST )+ − (K1 − ST )+ − (K3 − ST )+ + C (191) S∗down = K3 + C (192) S∗up = K1 − C (193) Pmax = C (194) Lmax = κ − C (195) 30 Ideally, this should be structured as a net credit trade, albeit this may not always be possible. 33 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.43"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.43 Strategy: Short put butterfly This is a volatility strategy consisting of a short position in an ITM put option with a strike price K1 , a long position in two ATM put options with a strike price K2 , and a short position in an OTM put option with a strike price K3 . The strikes are equidistant: K2 − K3 = K1 − K2 = κ. This is a net credit trade. In this sense, this is an income strategy. However, the potential reward is sizably smaller than with a short straddle or a short strangle (albeit with a lower risk). The trader’s outlook is neutral. We have: fT = 2 × (K2 − ST )+ − (K1 − ST )+ − (K3 − ST )+ + C (191) S∗down = K3 + C (192) S∗up = K1 − C (193) Pmax = C (194) Lmax = κ − C (195) 30 Ideally, this should be structured as a net credit trade, albeit this may not always be possible. 33 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze"


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
