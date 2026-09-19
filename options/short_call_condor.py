"""Short call condor.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.48, PDF p. 35, equations (216), (217), (218), (219), (220).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.48 Strategy: Short call condor This is a volatility strategy consisting of a short position in an ITM call option with a strike price K1 , a long position in an ITM call option with a higher strike price K2 , a long position in an OTM call option with a strike price K3 , and a short position in an OTM call option with a higher strike price K4 . All strikes are equidistant: K4 − K3 = K3 − K2 = K2 − K1 = κ. This is a relatively low net credit trade. As with a short call butterfly, the potential reward is sizably smaller than with a short straddle or a short strangle (albeit with a lower risk). So, this is a capital gain (rather than an income) strategy. The trader’s outlook is neutral. We have: fT = (ST − K2 )+ + (ST − K3 )+ − (ST − K1 )+ − (ST − K4 )+ + C (216) S∗up = K4 − C (217) S∗down = K1 + C (218) Pmax = C (219) Lmax = κ − C (220)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.48"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.48 Strategy: Short call condor This is a volatility strategy consisting of a short position in an ITM call option with a strike price K1 , a long position in an ITM call option with a higher strike price K2 , a long position in an OTM call option with a strike price K3 , and a short position in an OTM call option with a higher strike price K4 . All strikes are equidistant: K4 − K3 = K3 − K2 = K2 − K1 = κ. This is a relatively low net credit trade. As with a short call butterfly, the potential reward is sizably smaller than with a short straddle or a short strangle (albeit with a lower risk). So, this is a capital gain (rather than an income) strategy. The trader’s outlook is neutral. We have: fT = (ST − K2 )+ + (ST − K3 )+ − (ST − K1 )+ − (ST − K4 )+ + C (216) S∗up = K4 − C (217) S∗down = K1 + C (218) Pmax = C (219) Lmax = κ − C (220)"


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
