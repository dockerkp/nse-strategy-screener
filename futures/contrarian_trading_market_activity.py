"""Contrarian trading – market activity.

Source: Kakushadze & Serur, 151 Trading Strategies, §10.3.1, PDF p. 95.
Status: REFERENCE_ONLY.
Data requirements: futures prices by contract/expiry, hedge exposures, multipliers and roll dates.

Book rule summary: Implement the Contrarian trading – market activity construction described in the cited book section.
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "10.3.1"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "futures prices by contract/expiry, hedge exposures, multipliers and roll dates"
SIGNAL_RULE = "Implement the Contrarian trading – market activity construction described in the cited book section."


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
