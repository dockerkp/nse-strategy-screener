"""CDOs – curve trades.

Source: Kakushadze & Serur, 151 Trading Strategies, §11.6, PDF p. 100.
Status: REFERENCE_ONLY.
Data requirements: tranche/CDS/MBS cash flows, spreads, curves, defaults, prepayments and hedge quotes.

Book rule summary: Implement the CDOs – curve trades construction described in the cited book section.
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "11.6"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "tranche/CDS/MBS cash flows, spreads, curves, defaults, prepayments and hedge quotes"
SIGNAL_RULE = "Implement the CDOs – curve trades construction described in the cited book section."


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
                                                                            