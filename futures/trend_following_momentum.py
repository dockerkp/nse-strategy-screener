"""Trend following (momentum).

Source: Kakushadze & Serur, 151 Trading Strategies, §10.4, PDF p. 96.
Status: REFERENCE_ONLY.
Data requirements: futures prices by contract/expiry, hedge exposures, multipliers and roll dates.

Book rule summary: 4 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur. All Rights Reserved. 11 Structured Assets 97 11.1 Generalities: Collateralized Debt Obligations (CDOs) . . . . . . . . . 97
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "10.4"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "futures prices by contract/expiry, hedge exposures, multipliers and roll dates"
SIGNAL_RULE = "4 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur. All Rights Reserved. 11 Structured Assets 97 11.1 Generalities: Collateralized Debt Obligations (CDOs) . . . . . . . . . 97"


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
