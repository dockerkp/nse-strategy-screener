"""Short put condor.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.49, PDF p. 35, equations (221), (222), (223), (224), (225).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.49 Strategy: Short put condor This is a volatility strategy consisting of a short position in an OTM put option with a strike price K1 , a long position in an OTM put option with a higher strike price K2 , a long position in an ITM put option with a strike price K3 , and a short position in an ITM put option with a higher strike price K4 . All strikes are equidistant: K4 − K3 = K3 − K2 = K2 − K1 = κ. This is a relatively low net credit trade. 35 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur. All Rights Reserved. As with a short put butterfly, the potential reward is sizably smaller than with a short straddle or a short strangle (albeit with a lower risk). So, this is a capital gain (rather than an income) strategy. The trader’s outlook is neutral. We have: fT = (K2 − ST )+ + (K3 − ST )+ − (K1 − ST )+ − (K4 − ST
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.49"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.49 Strategy: Short put condor This is a volatility strategy consisting of a short position in an OTM put option with a strike price K1 , a long position in an OTM put option with a higher strike price K2 , a long position in an ITM put option with a strike price K3 , and a short position in an ITM put option with a higher strike price K4 . All strikes are equidistant: K4 − K3 = K3 − K2 = K2 − K1 = κ. This is a relatively low net credit trade. 35 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur. All Rights Reserved. As with a short put butterfly, the potential reward is sizably smaller than with a short straddle or a short strangle (albeit with a lower risk). So, this is a capital gain (rather than an income) strategy. The trader’s outlook is neutral. We have: fT = (K2 − ST )+ + (K3 − ST )+ − (K1 − ST )+ − (K4 − ST"


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
                                                                            