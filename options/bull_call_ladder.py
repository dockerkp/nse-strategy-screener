"""Bull call ladder.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.14, PDF p. 22, equations (53), (54), (55), (56), (57).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.14 Strategy: Bull call ladder This is a vertical spread consisting of a long position in (usually) a close to ATM call option with a strike price K1 , a short position in an OTM call option with a strike price K2 , and a short position in another OTM call option with a higher strike price K3 . A bull call ladder is a bull call spread financed by selling another OTM call option (with the strike price K3 ).18 This adjusts the trader’s outlook from bullish (bull call spread) to conservatively bullish or even non-directional (with an expectation of low volatility). We have: fT = (ST − K1 )+ − (ST − K2 )+ − (ST − K3 )+ − H (53) S∗down = K1 + H, H > 0 (54) S∗up = K3 + K2 − K1 − H (55) Pmax = K2 − K1 − H (56) Lmax = unlimited (57) 17 For some literature on long/short combo strategies, see, e.g., [Rusnáková, Šoltés and Szabo, 2015], [Šoltés, 2011], [Šoltés and Rusnáková, 2012]. Also
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.14"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.14 Strategy: Bull call ladder This is a vertical spread consisting of a long position in (usually) a close to ATM call option with a strike price K1 , a short position in an OTM call option with a strike price K2 , and a short position in another OTM call option with a higher strike price K3 . A bull call ladder is a bull call spread financed by selling another OTM call option (with the strike price K3 ).18 This adjusts the trader’s outlook from bullish (bull call spread) to conservatively bullish or even non-directional (with an expectation of low volatility). We have: fT = (ST − K1 )+ − (ST − K2 )+ − (ST − K3 )+ − H (53) S∗down = K1 + H, H > 0 (54) S∗up = K3 + K2 − K1 − H (55) Pmax = K2 − K1 − H (56) Lmax = unlimited (57) 17 For some literature on long/short combo strategies, see, e.g., [Rusnáková, Šoltés and Szabo, 2015], [Šoltés, 2011], [Šoltés and Rusnáková, 2012]. Also"


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
