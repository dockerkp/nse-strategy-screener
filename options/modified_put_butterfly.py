"""Modified put butterfly.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.41.1, PDF p. 33, equations (182), (183), (184), (185).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.41.1 Strategy: Modified put butterfly This is a variation of the long put butterfly strategy where the strikes are no longer equidistant; instead we have K3 − K2 < K2 − K1 . This results in a sideways strategy with a bullish bias. We have (for H > 0 there is also S∗up = K3 − H):30 fT = (K1 − ST )+ + (K3 − ST )+ − 2 × (K2 − ST )+ − H (182) S∗down = 2 × K2 − K3 + H (183) Pmax = K3 − K2 − H (184) Lmax = 2 × K2 − K1 − K3 + H (185)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.41.1"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.41.1 Strategy: Modified put butterfly This is a variation of the long put butterfly strategy where the strikes are no longer equidistant; instead we have K3 − K2 < K2 − K1 . This results in a sideways strategy with a bullish bias. We have (for H > 0 there is also S∗up = K3 − H):30 fT = (K1 − ST )+ + (K3 − ST )+ − 2 × (K2 − ST )+ − H (182) S∗down = 2 × K2 − K3 + H (183) Pmax = K3 − K2 − H (184) Lmax = 2 × K2 − K1 − K3 + H (185)"


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
