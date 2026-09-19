"""Short strangle.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.26, PDF p. 27, equations (101), (102), (103), (104), (105).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.26 Strategy: Short strangle This is a sideways strategy consisting of a short position in an OTM call option with a strike price K1 , and a short position in an OTM put option with a strike price K2 . This is a net credit trade. Since both call and put options are OTM, this strategy is less risky than a short straddle position. The flipside is that the initial credit is also lower. The trader’s outlook is neutral. This is an income strategy. We have: fT = −(ST − K1 )+ − (K2 − ST )+ + C (101) S∗up = K1 + C (102) S∗down = K2 − C (103) Pmax = C (104) Lmax = unlimited (105)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.26"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.26 Strategy: Short strangle This is a sideways strategy consisting of a short position in an OTM call option with a strike price K1 , and a short position in an OTM put option with a strike price K2 . This is a net credit trade. Since both call and put options are OTM, this strategy is less risky than a short straddle position. The flipside is that the initial credit is also lower. The trader’s outlook is neutral. This is an income strategy. We have: fT = −(ST − K1 )+ − (K2 − ST )+ + C (101) S∗up = K1 + C (102) S∗down = K2 − C (103) Pmax = C (104) Lmax = unlimited (105)"


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
