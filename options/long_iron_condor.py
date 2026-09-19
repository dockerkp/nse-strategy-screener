"""Long iron condor.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.50, PDF p. 36, equations (226), (227), (228), (229), (230).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.50 Strategy: Long iron condor This sideways strategy is a combination of a bull put spread and a bear call spread and consists of a long position in an OTM put option with a strike price K1 , a short position in an OTM put option with a higher strike price K2 , a short position in an OTM call option with a strike price K3 , and a long position in an OTM call option with a higher strike price K4 . The strikes are equidistant: K4 − K3 = K3 − K2 = K2 − K1 = κ. This is a net credit trade. The trader’s outlook is neutral. This is an income strategy. We have: fT = (K1 − ST )+ + (ST − K4 )+ − (K2 − ST )+ − (ST − K3 )+ + C (226) S∗up = K3 + C (227) S∗down = K2 − C (228) Pmax = C (229) Lmax = κ − C (230)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.50"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.50 Strategy: Long iron condor This sideways strategy is a combination of a bull put spread and a bear call spread and consists of a long position in an OTM put option with a strike price K1 , a short position in an OTM put option with a higher strike price K2 , a short position in an OTM call option with a strike price K3 , and a long position in an OTM call option with a higher strike price K4 . The strikes are equidistant: K4 − K3 = K3 − K2 = K2 − K1 = κ. This is a net credit trade. The trader’s outlook is neutral. This is an income strategy. We have: fT = (K1 − ST )+ + (ST − K4 )+ − (K2 − ST )+ − (ST − K3 )+ + C (226) S∗up = K3 + C (227) S∗down = K2 − C (228) Pmax = C (229) Lmax = κ − C (230)"


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
