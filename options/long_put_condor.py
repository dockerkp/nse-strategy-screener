"""Long put condor.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.47, PDF p. 35, equations (211), (212), (213), (214), (215).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.47 Strategy: Long put condor This is a sideways strategy consisting of a long position in an OTM put option with a strike price K1 , a short position in an OTM put option with a higher strike price K2 , a short position in an ITM put option with a strike price K3 , and a long position in an ITM put option with a higher strike price K4 . All strikes are equidistant: K4 − K3 = K3 − K2 = K2 − K1 = κ. This is a relatively low cost net debit trade. The trader’s outlook is neutral. This is a capital gain strategy. We have: fT = (K1 − ST )+ − (K2 − ST )+ − (K3 − ST )+ + (K4 − ST )+ − D (211) S∗up = K4 − D (212) S∗down = K1 + D (213) Pmax = κ − D (214) Lmax = D (215)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.47"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.47 Strategy: Long put condor This is a sideways strategy consisting of a long position in an OTM put option with a strike price K1 , a short position in an OTM put option with a higher strike price K2 , a short position in an ITM put option with a strike price K3 , and a long position in an ITM put option with a higher strike price K4 . All strikes are equidistant: K4 − K3 = K3 − K2 = K2 − K1 = κ. This is a relatively low cost net debit trade. The trader’s outlook is neutral. This is a capital gain strategy. We have: fT = (K1 − ST )+ − (K2 − ST )+ − (K3 − ST )+ + (K4 − ST )+ − D (211) S∗up = K4 − D (212) S∗down = K1 + D (213) Pmax = κ − D (214) Lmax = D (215)"


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
