"""Strap.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.34, PDF p. 30, equations (138), (139), (140), (141), (142).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.34 Strategy: Strap This is a volatility strategy consisting of a long position in two ATM call options, and a long position in an ATM put option with a strike price K. This is a net debit trade. The trader’s outlook is bullish. This is a capital gain strategy. We have:26 fT = 2 × (ST − K)+ + (K − ST )+ − D (138) D S∗up = K + (139) 2 S∗down = K − D (140) Pmax = unlimited (141) Lmax = D (142)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.34"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.34 Strategy: Strap This is a volatility strategy consisting of a long position in two ATM call options, and a long position in an ATM put option with a strike price K. This is a net debit trade. The trader’s outlook is bullish. This is a capital gain strategy. We have:26 fT = 2 × (ST − K)+ + (K − ST )+ − D (138) D S∗up = K + (139) 2 S∗down = K − D (140) Pmax = unlimited (141) Lmax = D (142)"


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
                                                                            