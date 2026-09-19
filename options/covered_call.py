"""Covered call.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.2, PDF p. 18, equations (1), (2), (3), (4).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.2 Strategy: Covered call This strategy (a.k.a. “buy-write” strategy) amounts to buying stock and writing a call option with a strike price K against the stock position. The trader’s outlook on the stock price is neutral to bullish. The covered call strategy has the same payoff as writing a put option (short/naked put).10 While maintaining the long stock position, the trader can generate income by periodically selling OTM call options. We have:11 fT = ST − S0 − (ST − K)+ + C = K − S0 − (K − ST )+ + C (1) S∗ = S0 − C (2) Pmax = K − S0 + C (3) Lmax = S0 − C (4)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.2"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.2 Strategy: Covered call This strategy (a.k.a. “buy-write” strategy) amounts to buying stock and writing a call option with a strike price K against the stock position. The trader’s outlook on the stock price is neutral to bullish. The covered call strategy has the same payoff as writing a put option (short/naked put).10 While maintaining the long stock position, the trader can generate income by periodically selling OTM call options. We have:11 fT = ST − S0 − (ST − K)+ + C = K − S0 − (K − ST )+ + C (1) S∗ = S0 − C (2) Pmax = K − S0 + C (3) Lmax = S0 − C (4)"


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
