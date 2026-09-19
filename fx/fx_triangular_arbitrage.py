"""FX triangular arbitrage.

Source: Kakushadze & Serur, 151 Trading Strategies, §8.5, PDF p. 89.
Status: REFERENCE_ONLY.
Data requirements: spot and forward FX rates, interest rates and synchronized currency quotes.

Book rule summary: 9 Commodities 89
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "8.5"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "spot and forward FX rates, interest rates and synchronized currency quotes"
SIGNAL_RULE = "9 Commodities 89"


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
