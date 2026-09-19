"""Repurchase agreement (REPO).

Source: Kakushadze & Serur, 151 Trading Strategies, §17.4, PDF p. 115.
Status: REFERENCE_ONLY.
Data requirements: cash balances, contractual rates/collateral, liquidity needs and applicable legal constraints.

Book rule summary: Implement the Repurchase agreement (REPO) construction described in the cited book section.
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "17.4"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "cash balances, contractual rates/collateral, liquidity needs and applicable legal constraints"
SIGNAL_RULE = "Implement the Repurchase agreement (REPO) construction described in the cited book section."


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
