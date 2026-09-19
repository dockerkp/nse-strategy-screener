"""Diagonal put spread.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.21, PDF p. 25, equations (79), (80).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.21 Strategy: Diagonal put spread This is a diagonal spread consisting of a long position in a deep ITM put option with a strike price K1 and TTM T 0 , and a short position in an OTM put option with a strike price K2 and shorter TTM T < T 0 . This is a net debit trade. The trader’s outlook is bearish. At t = T let V be the value of the long put option (expiring at t = T 0 ) assuming ST = K. We have: Pmax = V − D (79) Lmax = D (80) If at the expiration of the short put option the stock price K2 ≤ ST ≤ Sstop−loss , where Sstop−loss is the stop-loss price above which the trader would unwind the entire position, then the trader can write another OTM put option with TTM T1 < T 0 . While maintaining the long position in the put option with TTM T 0 , the trader can generate income by periodically selling OTM put options with shorter maturities. In this regard, this strategy is similar to the
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.21"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.21 Strategy: Diagonal put spread This is a diagonal spread consisting of a long position in a deep ITM put option with a strike price K1 and TTM T 0 , and a short position in an OTM put option with a strike price K2 and shorter TTM T < T 0 . This is a net debit trade. The trader’s outlook is bearish. At t = T let V be the value of the long put option (expiring at t = T 0 ) assuming ST = K. We have: Pmax = V − D (79) Lmax = D (80) If at the expiration of the short put option the stock price K2 ≤ ST ≤ Sstop−loss , where Sstop−loss is the stop-loss price above which the trader would unwind the entire position, then the trader can write another OTM put option with TTM T1 < T 0 . While maintaining the long position in the put option with TTM T 0 , the trader can generate income by periodically selling OTM put options with shorter maturities. In this regard, this strategy is similar to the"


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
