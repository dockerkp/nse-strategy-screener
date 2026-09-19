"""Multifactor portfolio.

Source: Kakushadze & Serur, 151 Trading Strategies, §3.6, PDF p. 43, equations (275), (276), (277).
Status: REFERENCE_ONLY.
Data requirements: completed stock OHLCV plus any fundamentals, events, sectors or options explicitly named by the rule.

Book rule summary: 3.6 Strategy: Multifactor portfolio This strategy amounts to buying and shorting stocks based on multiple factors such as value, momentum, etc. For instance, usually value and momentum are negatively correlated and combining them can add value (see, e.g., [Asness, Moskowitz and Pedersen, 2013]). There is a variety of ways in which F > 1 factors can be com- bined.46 The simplest way is to diversify the exposure to the F factors with some weights wA , where A = 1, . . . , F labels the factors. That is, if I is the total invest- ment level, then the F portfolios (each built as above based on the corresponding factor) are allocated the investment levels IA = wA ×I, where (assuming all wA > 0) F X wA = 1 (275) A=1 Thus, one can simply take uniform weights wA = 1/F , albeit this may not be the most optimal weighting scheme. E.g., similarly to Subsection 3.1, there are weighting Thorley,
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "3.6"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "completed stock OHLCV plus any fundamentals, events, sectors or options explicitly named by the rule"
SIGNAL_RULE = "3.6 Strategy: Multifactor portfolio This strategy amounts to buying and shorting stocks based on multiple factors such as value, momentum, etc. For instance, usually value and momentum are negatively correlated and combining them can add value (see, e.g., [Asness, Moskowitz and Pedersen, 2013]). There is a variety of ways in which F > 1 factors can be com- bined.46 The simplest way is to diversify the exposure to the F factors with some weights wA , where A = 1, . . . , F labels the factors. That is, if I is the total invest- ment level, then the F portfolios (each built as above based on the corresponding factor) are allocated the investment levels IA = wA ×I, where (assuming all wA > 0) F X wA = 1 (275) A=1 Thus, one can simply take uniform weights wA = 1/F , albeit this may not be the most optimal weighting scheme. E.g., similarly to Subsection 3.1, there are weighting Thorley,"


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
