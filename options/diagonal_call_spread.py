"""Diagonal call spread.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.20, PDF p. 25, equations (77), (78).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.20 Strategy: Diagonal call spread This is a diagonal spread consisting of a long position in a deep ITM call option with a strike price K1 and TTM T 0 , and a short position in an OTM call option with a strike price K2 and shorter TTM T < T 0 . This is a net debit trade. The trader’s outlook is bullish. At t = T let V be the value of the long call option (expiring at t = T 0 ) assuming ST = K. We have: Pmax = V − D (77) Lmax = D (78) If at the expiration of the short call option the stock price Sstop−loss ≤ ST ≤ K2 , where Sstop−loss is the stop-loss price below which the trader would unwind the entire position, then the trader can write another OTM call option with TTM T1 < T 0 . While maintaining the long position in the call option with TTM T 0 , the trader can generate income by periodically selling OTM call options with shorter maturities. In this regard, this strategy is similar
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.20"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.20 Strategy: Diagonal call spread This is a diagonal spread consisting of a long position in a deep ITM call option with a strike price K1 and TTM T 0 , and a short position in an OTM call option with a strike price K2 and shorter TTM T < T 0 . This is a net debit trade. The trader’s outlook is bullish. At t = T let V be the value of the long call option (expiring at t = T 0 ) assuming ST = K. We have: Pmax = V − D (77) Lmax = D (78) If at the expiration of the short call option the stock price Sstop−loss ≤ ST ≤ K2 , where Sstop−loss is the stop-loss price below which the trader would unwind the entire position, then the trader can write another OTM call option with TTM T1 < T 0 . While maintaining the long position in the call option with TTM T 0 , the trader can generate income by periodically selling OTM call options with shorter maturities. In this regard, this strategy is similar"


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
