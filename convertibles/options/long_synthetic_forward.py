"""Long synthetic forward.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.10, PDF p. 21, equations (33), (34), (35), (36).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.10 Strategy: Long synthetic forward This strategy amounts to buying an ATM call option and selling an ATM put option with a strike price K = S0 . This can be a net debit or net credit trade. Typically, |H| S0 . The trader’s outlook is bullish: this strategy mimics a long stock or futures position; it replicates a long forward contract with the delivery price K and the same maturity as the options. This is a capital gain strategy. We have:16 fT = (ST − K)+ − (K − ST )+ − H = ST − K − H (33) S∗ = K + H (34) Pmax = unlimited (35) Lmax = K + H (36)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.10"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.10 Strategy: Long synthetic forward This strategy amounts to buying an ATM call option and selling an ATM put option with a strike price K = S0 . This can be a net debit or net credit trade. Typically, |H| S0 . The trader’s outlook is bullish: this strategy mimics a long stock or futures position; it replicates a long forward contract with the delivery price K and the same maturity as the options. This is a capital gain strategy. We have:16 fT = (ST − K)+ − (K − ST )+ − H = ST − K − H (33) S∗ = K + H (34) Pmax = unlimited (35) Lmax = K + H (36)"


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
                                                                            