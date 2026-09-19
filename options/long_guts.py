"""Long guts.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.24, PDF p. 26, equations (91), (92), (93), (94), (95).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.24 Strategy: Long guts This is a volatility strategy consisting of a long position in an ITM call option with a strike price K1 , and a long position in an ITM put option with a strike price K2 . This is a net debit trade. Since both call and put options are ITM, this strategy 22 For some literature on straddle/strangle strategies, see, e.g., [Copeland and Galai, 1983], [Coval and Shumway, 2001], [Engle and Rosenberg, 2000], [Gao, Xing and Zhang, 2017], [Goltz and Lai, 2009], [Guo, 2000], [Hansch, Naik and Viswanathan, 1998], [Noh, Engle and Kane, 1994], [Rusnáková and Šoltés, 2012], [Suresh, 2015]. Academic literature specifically on long/short guts strategies (which can be thought of as variations on straddles) appears to be more scarce. For a book reference, see, e.g., [Cohen, 2005]. For covered straddles, see, e.g., [Johnson, 1979]. 26 Electronic copy available at:
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.24"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.24 Strategy: Long guts This is a volatility strategy consisting of a long position in an ITM call option with a strike price K1 , and a long position in an ITM put option with a strike price K2 . This is a net debit trade. Since both call and put options are ITM, this strategy 22 For some literature on straddle/strangle strategies, see, e.g., [Copeland and Galai, 1983], [Coval and Shumway, 2001], [Engle and Rosenberg, 2000], [Gao, Xing and Zhang, 2017], [Goltz and Lai, 2009], [Guo, 2000], [Hansch, Naik and Viswanathan, 1998], [Noh, Engle and Kane, 1994], [Rusnáková and Šoltés, 2012], [Suresh, 2015]. Academic literature specifically on long/short guts strategies (which can be thought of as variations on straddles) appears to be more scarce. For a book reference, see, e.g., [Cohen, 2005]. For covered straddles, see, e.g., [Johnson, 1979]. 26 Electronic copy available at:"


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
