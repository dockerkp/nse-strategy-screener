"""Bearish long seagull spread.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.55, PDF p. 38, equations (248), (249), (250), (251), (252), (253).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.55 Strategy: Bearish long seagull spread This option trading strategy is a short combo (short risk reversal) hedged against the stock price rising by buying an OTM call option. It amounts to a long position in an OTM put option with a strike price K1 , a short position in an ATM call option with a strike price K2 , and a long position in an OTM call option with a strike price K3 . Ideally, the trade should be structured to have zero cost. The trader’s outlook is bearish. This is a capital gain strategy. We have: fT = (K1 − ST )+ − (ST − K2 )+ + (ST − K3 )+ − H (248) S∗ = K1 − H, H > 0 (249) S∗ = K2 − H, H < 0 (250) K1 ≤ S∗ ≤ K2 , H = 0 (251) Pmax = K1 − H (252) Lmax = K3 − K2 + H (253)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.55"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.55 Strategy: Bearish long seagull spread This option trading strategy is a short combo (short risk reversal) hedged against the stock price rising by buying an OTM call option. It amounts to a long position in an OTM put option with a strike price K1 , a short position in an ATM call option with a strike price K2 , and a long position in an OTM call option with a strike price K3 . Ideally, the trade should be structured to have zero cost. The trader’s outlook is bearish. This is a capital gain strategy. We have: fT = (K1 − ST )+ − (ST − K2 )+ + (ST − K3 )+ − H (248) S∗ = K1 − H, H > 0 (249) S∗ = K2 − H, H < 0 (250) K1 ≤ S∗ ≤ K2 , H = 0 (251) Pmax = K1 − H (252) Lmax = K3 − K2 + H (253)"


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
