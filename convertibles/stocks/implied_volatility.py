"""Implied volatility.

Source: Kakushadze & Serur, 151 Trading Strategies, §3.5, PDF p. 43.
Status: REFERENCE_ONLY.
Data requirements: completed stock OHLCV plus any fundamentals, events, sectors or options explicitly named by the rule.

Book rule summary: 3.5 Strategy: Implied volatility This strategy is based on the empirical observation that stocks with larger increases in call implied volatilities over the previous month on average have higher future re- turns, while stocks with larger increases in put implied volatilities over the previous month on average have lower future returns (see, e.g., [An et al, 2014], [Chen, Chung and Tsai, 2016]).45 Therefore, the trader can, e.g., construct a dollar-neutral portfo- lio by buying stocks in the top decile by the increase in call implied volatilities, and shorting stocks in the top decile by the increase in put implied volatilities. One can also consider variations, e.g., buying stocks in the top decile by the difference twixt the change in call implied volatilities and the change in put implied volatilities.
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "3.5"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "completed stock OHLCV plus any fundamentals, events, sectors or options explicitly named by the rule"
SIGNAL_RULE = "3.5 Strategy: Implied volatility This strategy is based on the empirical observation that stocks with larger increases in call implied volatilities over the previous month on average have higher future re- turns, while stocks with larger increases in put implied volatilities over the previous month on average have lower future returns (see, e.g., [An et al, 2014], [Chen, Chung and Tsai, 2016]).45 Therefore, the trader can, e.g., construct a dollar-neutral portfo- lio by buying stocks in the top decile by the increase in call implied volatilities, and shorting stocks in the top decile by the increase in put implied volatilities. One can also consider variations, e.g., buying stocks in the top decile by the difference twixt the change in call implied volatilities and the change in put implied volatilities."


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
                                                                            