"""Short put synthetic straddle.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.31, PDF p. 29, equations (126), (127), (128), (129), (130).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.31 Strategy: Short put synthetic straddle This sideways strategy (which is the same as a short straddle with the call replaced by a synthetic call) amounts to shorting stock and selling two ATM (or the nearest OTM) put options with a strike price K. The trader’s outlook is neutral. This is a capital gain strategy. We have (assuming S0 ≥ K): fT = S0 − ST − 2 × (K − ST )+ + C (126) S∗up = S0 + C (127) S∗down = 2 × K − S0 − C (128) Pmax = S0 − K + C (129) Lmax = unlimited (130)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.31"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.31 Strategy: Short put synthetic straddle This sideways strategy (which is the same as a short straddle with the call replaced by a synthetic call) amounts to shorting stock and selling two ATM (or the nearest OTM) put options with a strike price K. The trader’s outlook is neutral. This is a capital gain strategy. We have (assuming S0 ≥ K): fT = S0 − ST − 2 × (K − ST )+ + C (126) S∗up = S0 + C (127) S∗down = 2 × K − S0 − C (128) Pmax = S0 − K + C (129) Lmax = unlimited (130)"


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
