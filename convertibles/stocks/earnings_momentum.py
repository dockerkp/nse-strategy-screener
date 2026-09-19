"""Earnings-momentum.

Source: Kakushadze & Serur, 151 Trading Strategies, §3.2, PDF p. 41, equations (0), (274).
Status: REFERENCE_ONLY.
Data requirements: completed stock OHLCV plus any fundamentals, events, sectors or options explicitly named by the rule.

Book rule summary: 3.2 Strategy: Earnings-momentum This strategy amounts to buying winners and selling losers as in the price-momentum strategy, but the selection criterion is based on earnings. One way to define such a 37 Albeit, e.g., a long-only portfolio may have to be liquidated before the end of this holding period due to unforeseen events, such as market crashes. 38 That is, assuming the stock is bought at the price Pi (0), which does not account for slippage. 39 For dollar-neutral portfolios IL = IS and I = 2 × IL . 40 For some additional literature on momentum strategies, see, e.g., [Antonacci, 2017], [Asem and Tian, 2010], [Barroso and Santa-Clara, 2014], [Bhojraj and Swaminathan, 2006], [Chordia and Shivakumar, 2002], [Chuang and Ho, 2014], [Cooper, Gutierrez and Hameed, 2004], [Daniel and Moskowitz, 2016], [Géczy and Samonov, 2016], [Griffin, Ji and Martin, 2003], [Grundy and Martin, 2001],
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "3.2"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "completed stock OHLCV plus any fundamentals, events, sectors or options explicitly named by the rule"
SIGNAL_RULE = "3.2 Strategy: Earnings-momentum This strategy amounts to buying winners and selling losers as in the price-momentum strategy, but the selection criterion is based on earnings. One way to define such a 37 Albeit, e.g., a long-only portfolio may have to be liquidated before the end of this holding period due to unforeseen events, such as market crashes. 38 That is, assuming the stock is bought at the price Pi (0), which does not account for slippage. 39 For dollar-neutral portfolios IL = IS and I = 2 × IL . 40 For some additional literature on momentum strategies, see, e.g., [Antonacci, 2017], [Asem and Tian, 2010], [Barroso and Santa-Clara, 2014], [Bhojraj and Swaminathan, 2006], [Chordia and Shivakumar, 2002], [Chuang and Ho, 2014], [Cooper, Gutierrez and Hameed, 2004], [Daniel and Moskowitz, 2016], [Géczy and Samonov, 2016], [Griffin, Ji and Martin, 2003], [Grundy and Martin, 2001],"


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
                                                                            