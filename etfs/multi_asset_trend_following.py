"""Multi-asset trend following.

Source: Kakushadze & Serur, 151 Trading Strategies, §4.6, PDF p. 65.
Status: REFERENCE_ONLY.
Data requirements: ETF total-return histories, holdings/exposures and a cash or benchmark series.

Book rule summary: 5 Fixed Income 66 5.1 Generalities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66 5.1.1 Zero-coupon bonds . . . . . . . . . . . . . . . . . . . . . . . . 66 5.1.2 Bonds with coupons . . . . . . . . . . . . . . . . . . . . . . . 66 5.1.3 Floating rate bonds . . . . . . . . . . . . . . . . . . . . . . . . 67 5.1.4 Swaps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67 5.1.5 Duration and convexity . . . . . . . . . . . . . . . . . . . . . . 68
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "4.6"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "ETF total-return histories, holdings/exposures and a cash or benchmark series"
SIGNAL_RULE = "5 Fixed Income 66 5.1 Generalities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66 5.1.1 Zero-coupon bonds . . . . . . . . . . . . . . . . . . . . . . . . 66 5.1.2 Bonds with coupons . . . . . . . . . . . . . . . . . . . . . . . 66 5.1.3 Floating rate bonds . . . . . . . . . . . . . . . . . . . . . . . . 67 5.1.4 Swaps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67 5.1.5 Duration and convexity . . . . . . . . . . . . . . . . . . . . . . 68"


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
