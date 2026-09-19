"""Call ratio backspread.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.36, PDF p. 30, equations (148), (149), (150), (151), (152).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.36 Strategy: Call ratio backspread This strategy consists of a short position in NS close to ATM call options with a strike price K1 , and a long position in NL OTM call options with a strike price K2 , where NL > NS . Typically, NL = 2 and NS = 1, or NL = 3 and NS = 2. The trader’s outlook is strongly bullish. This is a capital gain strategy. We have:27 fT = NL × (ST − K2 )+ − NS × (ST − K1 )+ − H (148) S∗down = K1 − H/NS , H < 0 (149) S∗up = (NL × K2 − NS × K1 + H)/(NL − NS ) (150) Pmax = unlimited (151) Lmax = NS × (K2 − K1 ) + H (152) 26 For some literature on strip and strap strategies, see, e.g., [Jha and Kalimipal, 2010], [Topaloglou, Vladimirou and Zenios, 2011]. 27 For some literature on call/put ratio (back)spreads, see, e.g., [Augustin, Brenner and Subrah- manyam, 2015], [Chaput and Ederington, 2008], [Šoltés, 2010], [Šoltés and Amaitiek, 2010b], [Šoltés and
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.36"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.36 Strategy: Call ratio backspread This strategy consists of a short position in NS close to ATM call options with a strike price K1 , and a long position in NL OTM call options with a strike price K2 , where NL > NS . Typically, NL = 2 and NS = 1, or NL = 3 and NS = 2. The trader’s outlook is strongly bullish. This is a capital gain strategy. We have:27 fT = NL × (ST − K2 )+ − NS × (ST − K1 )+ − H (148) S∗down = K1 − H/NS , H < 0 (149) S∗up = (NL × K2 − NS × K1 + H)/(NL − NS ) (150) Pmax = unlimited (151) Lmax = NS × (K2 − K1 ) + H (152) 26 For some literature on strip and strap strategies, see, e.g., [Jha and Kalimipal, 2010], [Topaloglou, Vladimirou and Zenios, 2011]. 27 For some literature on call/put ratio (back)spreads, see, e.g., [Augustin, Brenner and Subrah- manyam, 2015], [Chaput and Ederington, 2008], [Šoltés, 2010], [Šoltés and Amaitiek, 2010b], [Šoltés and"


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
