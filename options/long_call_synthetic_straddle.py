"""Long call synthetic straddle.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.28, PDF p. 28, equations (111), (112), (113), (114), (115).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.28 Strategy: Long call synthetic straddle This volatility strategy (which is the same as a long straddle with the put replaced by a synthetic put) amounts to shorting stock and buying two ATM (or the nearest ITM) call options with a strike price K. The trader’s outlook is neutral. This is a capital gain strategy.25 We have (assuming S0 ≥ K and D > S0 − K): fT = S0 − ST + 2 × (ST − K)+ − D (111) S∗up = 2 × K − S0 + D (112) S∗down = S0 − D (113) Pmax = unlimited (114) Lmax = D − (S0 − K) (115)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.28"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.28 Strategy: Long call synthetic straddle This volatility strategy (which is the same as a long straddle with the put replaced by a synthetic put) amounts to shorting stock and buying two ATM (or the nearest ITM) call options with a strike price K. The trader’s outlook is neutral. This is a capital gain strategy.25 We have (assuming S0 ≥ K and D > S0 − K): fT = S0 − ST + 2 × (ST − K)+ − D (111) S∗up = 2 × K − S0 + D (112) S∗down = S0 − D (113) Pmax = unlimited (114) Lmax = D − (S0 − K) (115)"


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
