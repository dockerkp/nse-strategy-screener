"""Value.

Source: Kakushadze & Serur, 151 Trading Strategies, §3.3, PDF p. 42.
Status: REFERENCE_ONLY.
Data requirements: completed stock OHLCV plus any fundamentals, events, sectors or options explicitly named by the rule.

Book rule summary: 3.3 Strategy: Value This strategy amounts to buying winners and selling losers as in the price-momentum and earnings-momentum strategies, but the selection criterion is based on value. Value can be defined as the Book-to-Price (B/P) ratio (see, e.g., [Rosenberg, Reid and Lanstein, 1985]). Here “Book” is the company’s book value per share outstand- ing (so the B/P ratio is the same as the Book-to-Market ratio, where now “Book” stands for its total book value, not per share outstanding, and “Market” is its market capitalization). The trader can, e.g., construct a zero-cost portfolio by buying stocks in the top decile by the B/P ratio, and shorting stocks in the bottom decile. There can be variations in the definition of the B/P ratio. Thus, e.g., [Asness, Moskowitz and Pedersen, 2013] uses current (i.e., most up-to-date) prices, while [Fama and French, 1992] and some others use prices
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "3.3"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "completed stock OHLCV plus any fundamentals, events, sectors or options explicitly named by the rule"
SIGNAL_RULE = "3.3 Strategy: Value This strategy amounts to buying winners and selling losers as in the price-momentum and earnings-momentum strategies, but the selection criterion is based on value. Value can be defined as the Book-to-Price (B/P) ratio (see, e.g., [Rosenberg, Reid and Lanstein, 1985]). Here “Book” is the company’s book value per share outstand- ing (so the B/P ratio is the same as the Book-to-Market ratio, where now “Book” stands for its total book value, not per share outstanding, and “Market” is its market capitalization). The trader can, e.g., construct a zero-cost portfolio by buying stocks in the top decile by the B/P ratio, and shorting stocks in the bottom decile. There can be variations in the definition of the B/P ratio. Thus, e.g., [Asness, Moskowitz and Pedersen, 2013] uses current (i.e., most up-to-date) prices, while [Fama and French, 1992] and some others use prices"


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
