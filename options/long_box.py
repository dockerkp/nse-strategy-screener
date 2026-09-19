"""Long box.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.52, PDF p. 37, equations (236), (237).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.52 Strategy: Long box This volatility strategy can be viewed as a combination of a long synthetic forward and a short synthetic forward, or as a combination of a bull call spread and a bear put spread, and consists of a long position in an ITM put option with a strike price K1 , a short position in an OTM put option with a lower strike price K2 , a long position in an ITM call option with the strike price K2 , and a short position in an OTM call option with the strike price K1 . The trader’s outlook is neutral. This is a capital gain strategy.31 We have (assuming K1 ≥ K2 + D): fT = (K1 − ST )+ − (K2 − ST )+ + (ST − K2 )+ − (ST − K1 )+ − D = K1 − K 2 − D (236) Pmax = (K1 − K2 ) − D (237)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.52"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.52 Strategy: Long box This volatility strategy can be viewed as a combination of a long synthetic forward and a short synthetic forward, or as a combination of a bull call spread and a bear put spread, and consists of a long position in an ITM put option with a strike price K1 , a short position in an OTM put option with a lower strike price K2 , a long position in an ITM call option with the strike price K2 , and a short position in an OTM call option with the strike price K1 . The trader’s outlook is neutral. This is a capital gain strategy.31 We have (assuming K1 ≥ K2 + D): fT = (K1 − ST )+ − (K2 − ST )+ + (ST − K2 )+ − (ST − K1 )+ − D = K1 − K 2 − D (236) Pmax = (K1 − K2 ) − D (237)"


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
