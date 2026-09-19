"""Bear call ladder.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.16, PDF p. 23, equations (63), (64), (65), (66), (67).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.16 Strategy: Bear call ladder This is a vertical spread consisting of a short position in (usually) a close to ATM call option with a strike price K1 , a long position in an OTM call option with a strike price K2 , and a long position in another OTM call option with a higher strike price K3 . A bear call ladder typically arises when a bear call spread (a bearish strategy) goes wrong (the stock trades higher), so the trader buys another OTM call option (with the strike price K3 ) to adjust the position to bullish. We have: fT = (ST − K3 )+ + (ST − K2 )+ − (ST − K1 )+ − H (63) S∗down = K1 − H, H < 0 (64) S∗up = K3 + K2 − K1 + H (65) Pmax = unlimited (66) Lmax = K2 − K1 + H (67)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.16"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.16 Strategy: Bear call ladder This is a vertical spread consisting of a short position in (usually) a close to ATM call option with a strike price K1 , a long position in an OTM call option with a strike price K2 , and a long position in another OTM call option with a higher strike price K3 . A bear call ladder typically arises when a bear call spread (a bearish strategy) goes wrong (the stock trades higher), so the trader buys another OTM call option (with the strike price K3 ) to adjust the position to bullish. We have: fT = (ST − K3 )+ + (ST − K2 )+ − (ST − K1 )+ − H (63) S∗down = K1 − H, H < 0 (64) S∗up = K3 + K2 − K1 + H (65) Pmax = unlimited (66) Lmax = K2 − K1 + H (67)"


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
