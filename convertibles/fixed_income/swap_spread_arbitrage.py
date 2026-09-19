"""Swap-spread arbitrage.

Source: Kakushadze & Serur, 151 Trading Strategies, §5.15, PDF p. 76.
Status: REFERENCE_ONLY.
Data requirements: bond prices, coupons, maturities, yields, durations, curves and financing rates.

Book rule summary: 3 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur. All Rights Reserved. 6 Indexes 76 6.1 Generalities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "5.15"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "bond prices, coupons, maturities, yields, durations, curves and financing rates"
SIGNAL_RULE = "3 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur. All Rights Reserved. 6 Indexes 76 6.1 Generalities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76"


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
                                                                            