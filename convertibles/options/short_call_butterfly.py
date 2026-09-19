"""Short call butterfly.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.42, PDF p. 33, equations (186), (187), (188), (189), (190).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.42 Strategy: Short call butterfly This is a volatility strategy consisting of a short position in an ITM call option with a strike price K1 , a long position in two ATM call options with a strike price K2 , and a short position in an OTM call option with a strike price K3 . The strikes are equidistant: K3 − K2 = K2 − K1 = κ. This is a net credit trade. In this sense, this is an income strategy. However, the potential reward is sizably smaller than with a short straddle or a short strangle (albeit with a lower risk). The trader’s outlook is neutral. We have: fT = 2 × (ST − K2 )+ − (ST − K1 )+ − (ST − K3 )+ + C (186) S∗up = K3 − C (187) S∗down = K1 + C (188) Pmax = C (189) Lmax = κ − C (190)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.42"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.42 Strategy: Short call butterfly This is a volatility strategy consisting of a short position in an ITM call option with a strike price K1 , a long position in two ATM call options with a strike price K2 , and a short position in an OTM call option with a strike price K3 . The strikes are equidistant: K3 − K2 = K2 − K1 = κ. This is a net credit trade. In this sense, this is an income strategy. However, the potential reward is sizably smaller than with a short straddle or a short strangle (albeit with a lower risk). The trader’s outlook is neutral. We have: fT = 2 × (ST − K2 )+ − (ST − K1 )+ − (ST − K3 )+ + C (186) S∗up = K3 − C (187) S∗down = K1 + C (188) Pmax = C (189) Lmax = κ − C (190)"


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
                                                                            