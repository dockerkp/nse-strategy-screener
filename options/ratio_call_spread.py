"""Ratio call spread.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.38, PDF p. 31, equations (158), (159), (160), (161), (162).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.38 Strategy: Ratio call spread This strategy consists of a short position in NS close to ATM call options with a strike price K1 , and a long position in NL ITM call options with a strike price K2 , where NL < NS . Typically, NL = 1 and NS = 2, or NL = 2 and NS = 3. This is an income strategy if it is structured as a net credit trade. The trader’s outlook is neutral to bearish. We have:28 fT = NL × (ST − K2 )+ − NS × (ST − K1 )+ − H (158) S∗down = K2 + H/NL , H > 0 (159) S∗up = (NS × K1 − NL × K2 − H)/(NS − NL ) (160) Pmax = NL × (K1 − K2 ) − H (161) Lmax = unlimited (162)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.38"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.38 Strategy: Ratio call spread This strategy consists of a short position in NS close to ATM call options with a strike price K1 , and a long position in NL ITM call options with a strike price K2 , where NL < NS . Typically, NL = 1 and NS = 2, or NL = 2 and NS = 3. This is an income strategy if it is structured as a net credit trade. The trader’s outlook is neutral to bearish. We have:28 fT = NL × (ST − K2 )+ − NS × (ST − K1 )+ − H (158) S∗down = K2 + H/NL , H > 0 (159) S∗up = (NS × K1 − NL × K2 − H)/(NS − NL ) (160) Pmax = NL × (K1 − K2 ) − H (161) Lmax = unlimited (162)"


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
