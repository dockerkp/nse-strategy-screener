"""Buying outstanding debt.

Source: Kakushadze & Serur, 151 Trading Strategies, §15.2.2, PDF p. 109.
Status: REFERENCE_ONLY.
Data requirements: debt prices/terms, capital structure, recovery scenarios and restructuring events.

Book rule summary: Implement the Buying outstanding debt construction described in the cited book section.
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "15.2.2"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "debt prices/terms, capital structure, recovery scenarios and restructuring events"
SIGNAL_RULE = "Implement the Buying outstanding debt construction described in the cited book section."


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
