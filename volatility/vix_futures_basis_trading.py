"""VIX futures basis trading.

Source: Kakushadze & Serur, 151 Trading Strategies, §7.2, PDF p. 81.
Status: REFERENCE_ONLY.
Data requirements: VIX/volatility instruments, option surfaces, futures curves and hedge prices.

Book rule summary: Implement the VIX futures basis trading construction described in the cited book section.
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "7.2"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "VIX/volatility instruments, option surfaces, futures curves and hedge prices"
SIGNAL_RULE = "Implement the VIX futures basis trading construction described in the cited book section."


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
