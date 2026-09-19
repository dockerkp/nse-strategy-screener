"""Short synthetic forward.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.11, PDF p. 21, equations (37), (38), (39), (40).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.11 Strategy: Short synthetic forward This strategy amounts to buying an ATM put option and selling an ATM call option with a strike price K = S0 . This can be a net debit or net credit trade. Typically, |H| S0 . The trader’s outlook is bearish: this strategy mimics a short stock or futures position; it replicates a short forward contract with the delivery price K and the same maturity as the options. This is a capital gain strategy. We have: fT = (K − ST )+ − (ST − K)+ − H = K − ST − H (37) S∗ = K − H (38) Pmax = K − H (39) Lmax = unlimited (40)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.11"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.11 Strategy: Short synthetic forward This strategy amounts to buying an ATM put option and selling an ATM call option with a strike price K = S0 . This can be a net debit or net credit trade. Typically, |H| S0 . The trader’s outlook is bearish: this strategy mimics a short stock or futures position; it replicates a short forward contract with the delivery price K and the same maturity as the options. This is a capital gain strategy. We have: fT = (K − ST )+ − (ST − K)+ − H = K − ST − H (37) S∗ = K − H (38) Pmax = K − H (39) Lmax = unlimited (40)"


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
                                                                            