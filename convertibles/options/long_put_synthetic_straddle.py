"""Long put synthetic straddle.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.29, PDF p. 28, equations (116), (117), (118), (119), (120).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.29 Strategy: Long put synthetic straddle This volatility strategy (which is the same as a long straddle with the call replaced by a synthetic call) amounts to buying stock and buying two ATM (or the nearest ITM) put options with a strike price K. The trader’s outlook is neutral. This is a capital gain strategy. We have (assuming S0 ≤ K and D > K − S0 ): fT = ST − S0 + 2 × (K − ST )+ − D (116) S∗up = S0 + D (117) S∗down = 2 × K − S0 − D (118) Pmax = unlimited (119) Lmax = D − (K − S0 ) (120)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.29"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.29 Strategy: Long put synthetic straddle This volatility strategy (which is the same as a long straddle with the call replaced by a synthetic call) amounts to buying stock and buying two ATM (or the nearest ITM) put options with a strike price K. The trader’s outlook is neutral. This is a capital gain strategy. We have (assuming S0 ≤ K and D > K − S0 ): fT = ST − S0 + 2 × (K − ST )+ − D (116) S∗up = S0 + D (117) S∗down = 2 × K − S0 − D (118) Pmax = unlimited (119) Lmax = D − (K − S0 ) (120)"


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
                                                                            