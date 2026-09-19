"""Trading with pricing models.

Source: Kakushadze & Serur, 151 Trading Strategies, §9.6, PDF p. 91.
Status: REFERENCE_ONLY.
Data requirements: spot/futures curves, inventories or positioning data explicitly named by the rule.

Book rule summary: 10 Futures 92
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "9.6"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "spot/futures curves, inventories or positioning data explicitly named by the rule"
SIGNAL_RULE = "10 Futures 92"


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
