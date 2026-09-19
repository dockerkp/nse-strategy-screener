"""Bull put ladder.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.15, PDF p. 23, equations (58), (59), (60), (61), (62).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.15 Strategy: Bull put ladder This is a vertical spread consisting of a short position in (usually) a close to ATM put option with a strike price K1 , a long position in an OTM put option with a strike price K2 , and a long position in another OTM put option with a lower strike price K3 . A bull put ladder typically arises when a bull put spread (a bullish strategy) goes wrong (the stock trades lower), so the trader buys another OTM put option (with the strike price K3 ) to adjust the position to bearish. We have:19 fT = (K3 − ST )+ + (K2 − ST )+ − (K1 − ST )+ − H (58) S∗up = K1 + H, H < 0 (59) S∗down = K3 + K2 − K1 − H (60) Pmax = K3 + K2 − K1 − H (61) Lmax = K1 − K2 + H (62)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.15"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.15 Strategy: Bull put ladder This is a vertical spread consisting of a short position in (usually) a close to ATM put option with a strike price K1 , a long position in an OTM put option with a strike price K2 , and a long position in another OTM put option with a lower strike price K3 . A bull put ladder typically arises when a bull put spread (a bullish strategy) goes wrong (the stock trades lower), so the trader buys another OTM put option (with the strike price K3 ) to adjust the position to bearish. We have:19 fT = (K3 − ST )+ + (K2 − ST )+ − (K1 − ST )+ − H (58) S∗up = K1 + H, H < 0 (59) S∗down = K3 + K2 − K1 − H (60) Pmax = K3 + K2 − K1 − H (61) Lmax = K1 − K2 + H (62)"


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
