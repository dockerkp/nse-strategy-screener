"""Residual momentum.

Source: Kakushadze & Serur, 151 Trading Strategies, §3.7, PDF p. 44, equations (278), (279), (280), (281), (282).
Status: REFERENCE_ONLY.
Data requirements: completed stock OHLCV plus any fundamentals, events, sectors or options explicitly named by the rule.

Book rule summary: 3.7 Strategy: Residual momentum This is the same as the price-momentum strategy with the stock returns Ri (t) re- placed by the residuals i (t) of a serial regression of the stock returns Ri (t) over, e.g., the 3 Fama-French factors MKT(t), SMB(t), HML(t),50 with the intercept (see, 47 Another approach is to fix the weights wA by optimizing a portfolio of the F expected returns corresponding to the F factors (using an invertible F × F covariance matrix for these returns). 48 These two ways generally do not produce the same resultant portfolios. 49 For additional literature on multifactor strategies, see, e.g., [Amenc et al, 2016], [Amenc et al, 2015], [Arnott et al, 2013], [Asness, 1997], [Barber, Bennett and Gvozdeva, 2015], [Cochrane, 1999], [Fama, 1996], [Grinold and Kahn, 2000], [Hsu, Lin and Vincent, 2018], [Kahn and Lemmon, 2015], [Kahn and Lemmon, 2016], [Kozlov and Petajisto,
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "3.7"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "completed stock OHLCV plus any fundamentals, events, sectors or options explicitly named by the rule"
SIGNAL_RULE = "3.7 Strategy: Residual momentum This is the same as the price-momentum strategy with the stock returns Ri (t) re- placed by the residuals i (t) of a serial regression of the stock returns Ri (t) over, e.g., the 3 Fama-French factors MKT(t), SMB(t), HML(t),50 with the intercept (see, 47 Another approach is to fix the weights wA by optimizing a portfolio of the F expected returns corresponding to the F factors (using an invertible F × F covariance matrix for these returns). 48 These two ways generally do not produce the same resultant portfolios. 49 For additional literature on multifactor strategies, see, e.g., [Amenc et al, 2016], [Amenc et al, 2015], [Arnott et al, 2013], [Asness, 1997], [Barber, Bennett and Gvozdeva, 2015], [Cochrane, 1999], [Fama, 1996], [Grinold and Kahn, 2000], [Hsu, Lin and Vincent, 2018], [Kahn and Lemmon, 2015], [Kahn and Lemmon, 2016], [Kozlov and Petajisto,"


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
                                                                            