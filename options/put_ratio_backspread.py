"""Put ratio backspread.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.37, PDF p. 31, equations (153), (154), (155), (156), (157).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.37 Strategy: Put ratio backspread This strategy consists of a short position in NS close to ATM put options with a strike price K1 , and a long position in NL OTM put options with a strike price K2 , where NL > NS . Typically, NL = 2 and NS = 1, or NL = 3 and NS = 2. The trader’s outlook is strongly bearish. This is a capital gain strategy. We have: fT = NL × (K2 − ST )+ − NS × (K1 − ST )+ − H (153) S∗up = K1 + H/NS , H < 0 (154) S∗down = (NL × K2 − NS × K1 − H)/(NL − NS ) (155) Pmax = NL × K2 − NS × K1 − H (156) Lmax = NS × (K1 − K2 ) + H (157)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.37"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.37 Strategy: Put ratio backspread This strategy consists of a short position in NS close to ATM put options with a strike price K1 , and a long position in NL OTM put options with a strike price K2 , where NL > NS . Typically, NL = 2 and NS = 1, or NL = 3 and NS = 2. The trader’s outlook is strongly bearish. This is a capital gain strategy. We have: fT = NL × (K2 − ST )+ − NS × (K1 − ST )+ − H (153) S∗up = K1 + H/NS , H < 0 (154) S∗down = (NL × K2 − NS × K1 − H)/(NL − NS ) (155) Pmax = NL × K2 − NS × K1 − H (156) Lmax = NS × (K1 − K2 ) + H (157)"


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
