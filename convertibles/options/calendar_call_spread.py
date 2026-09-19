"""Calendar put spread.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.19, PDF p. 24, equations (75), (76).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.19 Strategy: Calendar put spread This is a horizontal spread consisting of a long position in a close to ATM put option with TTM T 0 and a short position in another put option with the same strike price K but shorter TTM T < T 0 . This is a net debit trade. The trader’s outlook is neutral to bearish. At the expiration of the short put option (t = T ), the best case scenario is if the stock price is right at the strike price (ST = K). At t = T let V be the value of the long put option (expiring at t = T 0 ) assuming ST = K. We have: Pmax = V − D (75) Lmax = D (76) If at the expiration of the short put option the stock price K ≤ ST ≤ Sstop−loss , where Sstop−loss is the stop-loss price above which the trader would unwind the 21 For some literature on calendar/diagonal call/put spreads, see, e.g., [Carmona and Durrleman, 2003], [Carr and Javaheri, 2005], [Dale and Currie, 2015],
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.19"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.19 Strategy: Calendar put spread This is a horizontal spread consisting of a long position in a close to ATM put option with TTM T 0 and a short position in another put option with the same strike price K but shorter TTM T < T 0 . This is a net debit trade. The trader’s outlook is neutral to bearish. At the expiration of the short put option (t = T ), the best case scenario is if the stock price is right at the strike price (ST = K). At t = T let V be the value of the long put option (expiring at t = T 0 ) assuming ST = K. We have: Pmax = V − D (75) Lmax = D (76) If at the expiration of the short put option the stock price K ≤ ST ≤ Sstop−loss , where Sstop−loss is the stop-loss price above which the trader would unwind the 21 For some literature on calendar/diagonal call/put spreads, see, e.g., [Carmona and Durrleman, 2003], [Carr and Javaheri, 2005], [Dale and Currie, 2015],"


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
                                                                            