"""Ratio put spread.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.39, PDF p. 31, equations (163), (164), (165), (166), (167).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.39 Strategy: Ratio put spread This strategy consists of a short position in NS close to ATM put options with a strike price K1 , and a long position in NL ITM put options with a strike price K2 , where NL < NS . Typically, NL = 1 and NS = 2, or NL = 2 and NS = 3. This is an income strategy if it is structured as a net credit trade. The trader’s outlook is neutral to bullish. We have: fT = NL × (K2 − ST )+ − NS × (K1 − ST )+ − H (163) S∗up = K2 − H/NL , H > 0 (164) S∗down = (NS × K1 − NL × K2 + H)/(NS − NL ) (165) Pmax = NL × (K2 − K1 ) − H (166) Lmax = NS × K1 − NL × K2 + H (167) 28 So, the difference between call/put ratio backspreads and ratio call/put spreads is that in the former NL > NS , while in the latter NL < NS . 31 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur. All Rights Reserved.
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.39"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.39 Strategy: Ratio put spread This strategy consists of a short position in NS close to ATM put options with a strike price K1 , and a long position in NL ITM put options with a strike price K2 , where NL < NS . Typically, NL = 1 and NS = 2, or NL = 2 and NS = 3. This is an income strategy if it is structured as a net credit trade. The trader’s outlook is neutral to bullish. We have: fT = NL × (K2 − ST )+ − NS × (K1 − ST )+ − H (163) S∗up = K2 − H/NL , H > 0 (164) S∗down = (NS × K1 − NL × K2 + H)/(NS − NL ) (165) Pmax = NL × (K2 − K1 ) − H (166) Lmax = NS × K1 − NL × K2 + H (167) 28 So, the difference between call/put ratio backspreads and ratio call/put spreads is that in the former NL > NS , while in the latter NL < NS . 31 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur. All Rights Reserved."


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
                                                                            