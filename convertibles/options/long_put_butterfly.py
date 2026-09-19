"""Short combo.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.13, PDF p. 22, equations (47), (48), (49), (50), (51), (52).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.13 Strategy: Short combo This strategy (a.k.a. “short risk reversal”) amounts to buying an OTM put option with a strike price K1 and selling an OTM call option with a strike price K2 . The trader’s outlook is bearish. This is a capital gain strategy. We have (K2 > K1 ): fT = (K1 − ST )+ − (ST − K2 )+ − H (47) S∗ = K1 − H, H > 0 (48) S∗ = K2 − H, H < 0 (49) K1 ≤ S∗ ≤ K2 , H = 0 (50) Pmax = K1 − H (51) Lmax = unlimited (52)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.13"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.13 Strategy: Short combo This strategy (a.k.a. “short risk reversal”) amounts to buying an OTM put option with a strike price K1 and selling an OTM call option with a strike price K2 . The trader’s outlook is bearish. This is a capital gain strategy. We have (K2 > K1 ): fT = (K1 − ST )+ − (ST − K2 )+ − H (47) S∗ = K1 − H, H > 0 (48) S∗ = K2 − H, H < 0 (49) K1 ≤ S∗ ≤ K2 , H = 0 (50) Pmax = K1 − H (51) Lmax = unlimited (52)"


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
                                                                            