"""Protective call.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.5, PDF p. 19, equations (13), (14), (15), (16).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.5 Strategy: Protective call This strategy (a.k.a. “married call” or “synthetic put”) amounts to shorting stock and buying an ATM or OTM call option with a strike price K ≥ S0 . The trader’s outlook is bearish. This is a hedging strategy: the call option hedges the risk of the stock price rising. We have:14 fT = S0 − ST + (ST − K)+ − D = S0 − K + (K − ST )+ − D (13) S∗ = S0 − D (14) Pmax = S0 − D (15) Lmax = K − S0 + D (16)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.5"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.5 Strategy: Protective call This strategy (a.k.a. “married call” or “synthetic put”) amounts to shorting stock and buying an ATM or OTM call option with a strike price K ≥ S0 . The trader’s outlook is bearish. This is a hedging strategy: the call option hedges the risk of the stock price rising. We have:14 fT = S0 − ST + (ST − K)+ − D = S0 − K + (K − ST )+ − D (13) S∗ = S0 − D (14) Pmax = S0 − D (15) Lmax = K − S0 + D (16)"


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
                                                                            