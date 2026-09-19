"""Collar.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.53, PDF p. 37, equations (238), (239), (240), (241).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.53 Strategy: Collar This strategy (a.k.a. “fence”) is a covered call augmented by a long put option as insurance against the stock price falling.32 It amounts to buying stock, buying an OTM put option with a strike price K1 , and selling an OTM call option with a higher strike price K2 . The trader’s outlook is moderately bullish. This is a capital gain strategy. We have:33 fT = ST − S0 + (K1 − ST )+ − (ST − K2 )+ − H (238) S∗ = S0 + H (239) Pmax = K2 − S0 − H (240) Lmax = S0 − K1 + H (241)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.53"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.53 Strategy: Collar This strategy (a.k.a. “fence”) is a covered call augmented by a long put option as insurance against the stock price falling.32 It amounts to buying stock, buying an OTM put option with a strike price K1 , and selling an OTM call option with a higher strike price K2 . The trader’s outlook is moderately bullish. This is a capital gain strategy. We have:33 fT = ST − S0 + (K1 − ST )+ − (ST − K2 )+ − H (238) S∗ = S0 + H (239) Pmax = K2 − S0 − H (240) Lmax = S0 − K1 + H (241)"


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
                                                                            