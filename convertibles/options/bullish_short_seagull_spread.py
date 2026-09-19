"""Bullish short seagull spread.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.54, PDF p. 37, equations (242), (243), (244), (245), (246), (247).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.54 Strategy: Bullish short seagull spread This option trading strategy is a bull call spread financed with a sale of an OTM put option. It amounts to a short position in an OTM put option with a strike price K1 , a long position in an ATM call option with a strike price K2 , and a short position in an OTM call option with a strike price K3 . Ideally, the trade should be structured to have zero cost. The trader’s outlook is bullish. This is a capital gain 31 In some cases it can be used as a tax strategy – see, e.g., [Cohen, 2005]. For some literature on box option strategies, see, e.g., [BenZion, Anan and Yagil, 2005], [Bharadwaj and Wiggins, 2001], [Billingsley and Chance, 1985], [Clarke, de Silva and Thorley, 2013], [Fung, Mok and Wong, 2004], [Hemler and Miller, 1997], [Jongadsayakul, 2016], [Ronn and Ronn, 1989], [Vipul, 2009]. 32 Similarly, a short collar is a covered put
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.54"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.54 Strategy: Bullish short seagull spread This option trading strategy is a bull call spread financed with a sale of an OTM put option. It amounts to a short position in an OTM put option with a strike price K1 , a long position in an ATM call option with a strike price K2 , and a short position in an OTM call option with a strike price K3 . Ideally, the trade should be structured to have zero cost. The trader’s outlook is bullish. This is a capital gain 31 In some cases it can be used as a tax strategy – see, e.g., [Cohen, 2005]. For some literature on box option strategies, see, e.g., [BenZion, Anan and Yagil, 2005], [Bharadwaj and Wiggins, 2001], [Billingsley and Chance, 1985], [Clarke, de Silva and Thorley, 2013], [Fung, Mok and Wong, 2004], [Hemler and Miller, 1997], [Jongadsayakul, 2016], [Ronn and Ronn, 1989], [Vipul, 2009]. 32 Similarly, a short collar is a covered put"


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
                                                                            