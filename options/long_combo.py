"""Long combo.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.12, PDF p. 21, equations (41), (42), (43), (44), (45), (46).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.12 Strategy: Long combo This strategy (a.k.a. “long risk reversal”) amounts to buying an OTM call option with a strike price K1 and selling an OTM put option with a strike price K2 . The 16 For some literature on long/short synthetic forward contracts (a.k.a. synthetic futures), see, e.g., [Benavides, 2009], [Bozic and Fortenbery, 2012], [DeMaskey, 1995], [Ebrahim and Rahman, 2005], [Nandy and Chattopadhyay, 2016]. 21 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur. All Rights Reserved. trader’s outlook is bullish. This is a capital gain strategy.17 We have (K1 > K2 ): fT = (ST − K1 )+ − (K2 − ST )+ − H (41) S∗ = K1 + H, H > 0 (42) S∗ = K2 + H, H < 0 (43) K2 ≤ S∗ ≤ K1 , H = 0 (44) Pmax = unlimited (45) Lmax = K2 + H (46)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.12"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.12 Strategy: Long combo This strategy (a.k.a. “long risk reversal”) amounts to buying an OTM call option with a strike price K1 and selling an OTM put option with a strike price K2 . The 16 For some literature on long/short synthetic forward contracts (a.k.a. synthetic futures), see, e.g., [Benavides, 2009], [Bozic and Fortenbery, 2012], [DeMaskey, 1995], [Ebrahim and Rahman, 2005], [Nandy and Chattopadhyay, 2016]. 21 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur. All Rights Reserved. trader’s outlook is bullish. This is a capital gain strategy.17 We have (K1 > K2 ): fT = (ST − K1 )+ − (K2 − ST )+ − H (41) S∗ = K1 + H, H > 0 (42) S∗ = K2 + H, H < 0 (43) K2 ≤ S∗ ≤ K1 , H = 0 (44) Pmax = unlimited (45) Lmax = K2 + H (46)"


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
