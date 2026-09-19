"""Covered put.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.3, PDF p. 18, equations (5), (6), (7), (8).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.3 Strategy: Covered put This strategy (a.k.a. “sell-write” strategy) amounts to shorting stock and writing a put option with a strike price K against the stock position. The trader’s outlook is 9 H is the net debit for all bought option premia less the net credit for all sold option premia. 10 This is related to put-call parity (see, e.g., [Stoll, 1969], [Hull, 2012]). 11 For some literature on covered call strategies, see, e.g., [Pounds, 1978], [Whaley, 2002], [Feld- man and Roy, 2004], [Hill et al, 2006], [Kapadia and Szado, 2007], [Che and Fung, 2011], [Mugwagwa et al, 2012], [Israelov and Nielsen, 2014], [Israelov and Nielsen, 2015a], [Hemler and Miller, 2015]. 18 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur. All Rights Reserved. neutral to bearish. The covered put strategy has the same payoff as writing a
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.3"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.3 Strategy: Covered put This strategy (a.k.a. “sell-write” strategy) amounts to shorting stock and writing a put option with a strike price K against the stock position. The trader’s outlook is 9 H is the net debit for all bought option premia less the net credit for all sold option premia. 10 This is related to put-call parity (see, e.g., [Stoll, 1969], [Hull, 2012]). 11 For some literature on covered call strategies, see, e.g., [Pounds, 1978], [Whaley, 2002], [Feld- man and Roy, 2004], [Hill et al, 2006], [Kapadia and Szado, 2007], [Che and Fung, 2011], [Mugwagwa et al, 2012], [Israelov and Nielsen, 2014], [Israelov and Nielsen, 2015a], [Hemler and Miller, 2015]. 18 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur. All Rights Reserved. neutral to bearish. The covered put strategy has the same payoff as writing a"


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
