"""Bear put spread.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.9, PDF p. 20, equations (29), (30), (31), (32).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.9 Strategy: Bear put spread This is a vertical spread consisting of a long position in a close to ATM put option with a strike price K1 , and a short position in an OTM put option with a lower 15 For some literature on bull/bear call/put vertical spreads, see, e.g., [Cartea and Pedraz, 2012], [Chaput and Ederington, 2003], [Chaput and Ederington, 2005], [Chen, Chen and Howell, 1999], [Cong, Tan and Weng, 2013], [Cong, Tan and Weng, 2014], [Matsypura and Timkovsky, 2010], [Shah, 2017], [Wong, Thompson and Teh, 2011], [Zhang, 2015]. Also see [Clarke, de Silva and Thorley, 2013], [Cohen, 2005], [Jabbour and Budwick, 2010], [McMillan, 2002], [The Options Institute, 1995]. 20 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur. All Rights Reserved. strike price K2 . This is a net debit trade. The trader’s outlook is
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.9"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.9 Strategy: Bear put spread This is a vertical spread consisting of a long position in a close to ATM put option with a strike price K1 , and a short position in an OTM put option with a lower 15 For some literature on bull/bear call/put vertical spreads, see, e.g., [Cartea and Pedraz, 2012], [Chaput and Ederington, 2003], [Chaput and Ederington, 2005], [Chen, Chen and Howell, 1999], [Cong, Tan and Weng, 2013], [Cong, Tan and Weng, 2014], [Matsypura and Timkovsky, 2010], [Shah, 2017], [Wong, Thompson and Teh, 2011], [Zhang, 2015]. Also see [Clarke, de Silva and Thorley, 2013], [Cohen, 2005], [Jabbour and Budwick, 2010], [McMillan, 2002], [The Options Institute, 1995]. 20 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur. All Rights Reserved. strike price K2 . This is a net debit trade. The trader’s outlook is"


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
