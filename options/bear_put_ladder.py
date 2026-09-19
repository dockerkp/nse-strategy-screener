"""Bear put ladder.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.17, PDF p. 23, equations (68), (69), (70), (71), (72).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.17 Strategy: Bear put ladder This is a vertical spread consisting of a long position in (usually) a close to ATM put option with a strike price K1 , a short position in an OTM put option with a strike price K2 , and a short position in another OTM put option with a lower strike price K3 . A bear put ladder is a bear put spread financed by selling another OTM put option (with the strike price K3 ).20 This adjusts the trader’s outlook from bearish (bear put spread) to conservatively bearish or even non-directional (with an 19 For some literature on ladder strategies, see, e.g., [Amaitiek, Bálint and Rešovský, 2010], [Harčariková and Šoltés, 2016], [He, Tang and Zhang, 2016], [Šoltés and Amaitiek, 2010a]. 20 In this sense, as for the bull call ladder, this is an “income” strategy. 23 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.17"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.17 Strategy: Bear put ladder This is a vertical spread consisting of a long position in (usually) a close to ATM put option with a strike price K1 , a short position in an OTM put option with a strike price K2 , and a short position in another OTM put option with a lower strike price K3 . A bear put ladder is a bear put spread financed by selling another OTM put option (with the strike price K3 ).20 This adjusts the trader’s outlook from bearish (bear put spread) to conservatively bearish or even non-directional (with an 19 For some literature on ladder strategies, see, e.g., [Amaitiek, Bálint and Rešovský, 2010], [Harčariková and Šoltés, 2016], [He, Tang and Zhang, 2016], [Šoltés and Amaitiek, 2010a]. 20 In this sense, as for the bull call ladder, this is an “income” strategy. 23 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze"


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
