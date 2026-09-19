"""“Long” iron butterfly.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.44, PDF p. 34, equations (196), (197), (198), (199), (200).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.44 Strategy: “Long” iron butterfly This sideways strategy is a combination of a bull put spread and a bear call spread and consists of a long position in an OTM put option with a strike price K1 , a short position in an ATM put option and an ATM call option with a strike price K2 , and a long position in an OTM call option with a strike price K3 . The strikes are equidistant: K2 − K1 = K3 − K2 = κ. This is a net credit trade. The trader’s outlook is neutral. This is an income strategy. We have: fT = (K1 − ST )+ − (K2 − ST )+ − (ST − K2 )+ + (ST − K3 )+ + C (196) S∗up = K2 + C (197) S∗down = K2 − C (198) Pmax = C (199) Lmax = κ − C (200)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.44"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.44 Strategy: “Long” iron butterfly This sideways strategy is a combination of a bull put spread and a bear call spread and consists of a long position in an OTM put option with a strike price K1 , a short position in an ATM put option and an ATM call option with a strike price K2 , and a long position in an OTM call option with a strike price K3 . The strikes are equidistant: K2 − K1 = K3 − K2 = κ. This is a net credit trade. The trader’s outlook is neutral. This is an income strategy. We have: fT = (K1 − ST )+ − (K2 − ST )+ − (ST − K2 )+ + (ST − K3 )+ + C (196) S∗up = K2 + C (197) S∗down = K2 − C (198) Pmax = C (199) Lmax = κ − C (200)"


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
