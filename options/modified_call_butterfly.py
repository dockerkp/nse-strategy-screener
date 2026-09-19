"""Modified call butterfly.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.40.1, PDF p. 32, equations (173), (174), (175), (176).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.40.1 Strategy: Modified call butterfly This is a variation of the long call butterfly strategy where the strikes are no longer equidistant; instead we have K1 − K2 < K2 − K3 . This results in a sideways strategy with a bullish bias. We have: fT = (ST − K1 )+ + (ST − K3 )+ − 2 × (ST − K2 )+ − D (173) S∗ = K3 + D (174) Pmax = K2 − K3 − D (175) Lmax = D (176)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.40.1"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.40.1 Strategy: Modified call butterfly This is a variation of the long call butterfly strategy where the strikes are no longer equidistant; instead we have K1 − K2 < K2 − K3 . This results in a sideways strategy with a bullish bias. We have: fT = (ST − K1 )+ + (ST − K3 )+ − 2 × (ST − K2 )+ − D (173) S∗ = K3 + D (174) Pmax = K2 − K3 − D (175) Lmax = D (176)"


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
