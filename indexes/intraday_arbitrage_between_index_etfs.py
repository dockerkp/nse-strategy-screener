"""Intraday arbitrage between index ETFs.

Source: Kakushadze & Serur, 151 Trading Strategies, §6.4, PDF p. 79.
Status: REFERENCE_ONLY.
Data requirements: index/constituent prices, futures or ETF quotes, weights, rates and transaction costs.

Book rule summary: Implement the Intraday arbitrage between index ETFs construction described in the cited book section.
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "6.4"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "index/constituent prices, futures or ETF quotes, weights, rates and transaction costs"
SIGNAL_RULE = "Implement the Intraday arbitrage between index ETFs construction described in the cited book section."


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
