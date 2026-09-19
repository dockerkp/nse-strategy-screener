"""Bullish long seagull spread.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.57, PDF p. 39, equations (260), (261), (262), (263), (264), (265).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.57 Strategy: Bullish long seagull spread This option trading strategy is a long combo (long risk reversal) hedged against the stock price falling by buying an OTM put option. It amounts to a long position in an OTM put option with a strike price K1 , a short position in an ATM put option with a strike price K2 , and a long position in an OTM call option with a strike price K3 . Ideally, the trade should be structured to have zero cost. The trader’s outlook is bullish. This is a capital gain strategy. We have: fT = (K1 − ST )+ − (K2 − ST )+ + (ST − K3 )+ − H (260) S∗ = K3 + H, H > 0 (261) S∗ = K2 + H, H < 0 (262) K2 ≤ S∗ ≤ K3 , H = 0 (263) Pmax = unlimited (264) Lmax = K2 − K1 + H (265) 39 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur. All Rights Reserved. 3 Stocks
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.57"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.57 Strategy: Bullish long seagull spread This option trading strategy is a long combo (long risk reversal) hedged against the stock price falling by buying an OTM put option. It amounts to a long position in an OTM put option with a strike price K1 , a short position in an ATM put option with a strike price K2 , and a long position in an OTM call option with a strike price K3 . Ideally, the trade should be structured to have zero cost. The trader’s outlook is bullish. This is a capital gain strategy. We have: fT = (K1 − ST )+ − (K2 − ST )+ + (ST − K3 )+ − H (260) S∗ = K3 + H, H > 0 (261) S∗ = K2 + H, H < 0 (262) K2 ≤ S∗ ≤ K3 , H = 0 (263) Pmax = unlimited (264) Lmax = K2 − K1 + H (265) 39 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur. All Rights Reserved. 3 Stocks"


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
                                                                            