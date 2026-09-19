"""Bull call spread.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.6, PDF p. 19, equations (17), (18), (19), (20).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.6 Strategy: Bull call spread This is a vertical spread consisting of a long position in a close to ATM call option with a strike price K1 , and a short position in an OTM call option with a higher 12 The covered put option strategy is symmetrical to the covered call option strategy. Academic literature on the covered put option strategy appears to be scarce. See, e.g., [Che, 2016]. 13 For some literature on protective put strategies, see, e.g., [Figlewski, Chidambaran and Ka- plan, 1993], [Israelov and Nielsen, 2015b], [Israelov, Nielsen and Villalon, 2017], [Israelov, 2017]. 14 The protective call option strategy is symmetrical to the protective put option strategy. Academic literature on the protective call option strategy appears to be scarce. See, e.g., [Jabbour and Budwick, 2010], [Tokic, 2013]. 19 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.6"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.6 Strategy: Bull call spread This is a vertical spread consisting of a long position in a close to ATM call option with a strike price K1 , and a short position in an OTM call option with a higher 12 The covered put option strategy is symmetrical to the covered call option strategy. Academic literature on the covered put option strategy appears to be scarce. See, e.g., [Che, 2016]. 13 For some literature on protective put strategies, see, e.g., [Figlewski, Chidambaran and Ka- plan, 1993], [Israelov and Nielsen, 2015b], [Israelov, Nielsen and Villalon, 2017], [Israelov, 2017]. 14 The protective call option strategy is symmetrical to the protective put option strategy. Academic literature on the protective call option strategy appears to be scarce. See, e.g., [Jabbour and Budwick, 2010], [Tokic, 2013]. 19 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018"


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
                                                                            