"""Long strangle.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.23, PDF p. 26, equations (86), (87), (88), (89), (90).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.23 Strategy: Long strangle This is a volatility strategy consisting of a long position in an OTM call option with a strike price K1 , and a long position in an OTM put option with a strike price K2 . This is a net debit trade. However, because both call and put options are OTM, this strategy is less costly to establish than a long straddle position. The flipside is that the movement in the stock price required to reach one of the break-even points is also more significant. The trader’s outlook is neutral. This is a capital gain strategy. We have: fT = (ST − K1 )+ + (K2 − ST )+ − D (86) S∗up = K1 + D (87) S∗down = K2 − D (88) Pmax = unlimited (89) Lmax = D (90)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.23"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.23 Strategy: Long strangle This is a volatility strategy consisting of a long position in an OTM call option with a strike price K1 , and a long position in an OTM put option with a strike price K2 . This is a net debit trade. However, because both call and put options are OTM, this strategy is less costly to establish than a long straddle position. The flipside is that the movement in the stock price required to reach one of the break-even points is also more significant. The trader’s outlook is neutral. This is a capital gain strategy. We have: fT = (ST − K1 )+ + (K2 − ST )+ − D (86) S∗up = K1 + D (87) S∗down = K2 − D (88) Pmax = unlimited (89) Lmax = D (90)"


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
                                                                            