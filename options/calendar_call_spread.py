"""Calendar call spread.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.18, PDF p. 24, equations (73), (74).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.18 Strategy: Calendar call spread This is a horizontal spread consisting of a long position in a close to ATM call option with TTM T 0 and a short position in another call option with the same strike price K but shorter TTM T < T 0 . This is a net debit trade. The trader’s outlook is neutral to bullish. At the expiration of the short call option (t = T ), the best case scenario is if the stock price is right at the strike price (ST = K). At t = T let V be the value of the long call option (expiring at t = T 0 ) assuming ST = K. We have:21 Pmax = V − D (73) Lmax = D (74) If at the expiration of the short call option the stock price Sstop−loss ≤ ST ≤ K, where Sstop−loss is the stop-loss price below which the trader would unwind the entire position, then the trader can write another call option with the strike price K and TTM T1 < T 0 . While maintaining the long position in the call
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.18"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.18 Strategy: Calendar call spread This is a horizontal spread consisting of a long position in a close to ATM call option with TTM T 0 and a short position in another call option with the same strike price K but shorter TTM T < T 0 . This is a net debit trade. The trader’s outlook is neutral to bullish. At the expiration of the short call option (t = T ), the best case scenario is if the stock price is right at the strike price (ST = K). At t = T let V be the value of the long call option (expiring at t = T 0 ) assuming ST = K. We have:21 Pmax = V − D (73) Lmax = D (74) If at the expiration of the short call option the stock price Sstop−loss ≤ ST ≤ K, where Sstop−loss is the stop-loss price below which the trader would unwind the entire position, then the trader can write another call option with the strike price K and TTM T1 < T 0 . While maintaining the long position in the call"


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
