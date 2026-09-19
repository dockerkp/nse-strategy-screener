"""Mean-reversion – weighted regression.

Source: Kakushadze & Serur, 151 Trading Strategies, §3.10, PDF p. 49, equations (310), (313), (314), (315), (316), (317), (318).
Status: REFERENCE_ONLY.
Data requirements: completed stock OHLCV plus any fundamentals, events, sectors or options explicitly named by the rule.

Book rule summary: 3.10 Mean-reversion – weighted regression The conditions (310) satisfied by the demeaned returns when the loadings matrix is binary simply mean that these returns are cluster-neutral, i.e., orthogonal to the K N -vectors v (A) comprising the columns of ΛiA . Such orthogonality can be defined for any loadings matrix, not just a binary one. So, we can consider a generalization where the loadings matrix, call it ΩiA , may have some binary columns, but generally it need not. The binary columns, if any, can, e.g., be industry (or sector) based risk factors; the non-binary columns are interpreted as some non-industry based risk factors; and the orthogonality condition N X R ei ΩiA , A = 1, . . . , K (313) i=1 can be satisfied if the twiddled returns Rei are related to the residuals εi of the regression of Ri over ΩiA with some (generally nonuniform) regression weights zi via R e=Z ε (314) ε =
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "3.10"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "completed stock OHLCV plus any fundamentals, events, sectors or options explicitly named by the rule"
SIGNAL_RULE = "3.10 Mean-reversion – weighted regression The conditions (310) satisfied by the demeaned returns when the loadings matrix is binary simply mean that these returns are cluster-neutral, i.e., orthogonal to the K N -vectors v (A) comprising the columns of ΛiA . Such orthogonality can be defined for any loadings matrix, not just a binary one. So, we can consider a generalization where the loadings matrix, call it ΩiA , may have some binary columns, but generally it need not. The binary columns, if any, can, e.g., be industry (or sector) based risk factors; the non-binary columns are interpreted as some non-industry based risk factors; and the orthogonality condition N X R ei ΩiA , A = 1, . . . , K (313) i=1 can be satisfied if the twiddled returns Rei are related to the residuals εi of the regression of Ri over ΩiA with some (generally nonuniform) regression weights zi via R e=Z ε (314) ε ="


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
                                                                            