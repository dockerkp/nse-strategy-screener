"""Short call synthetic straddle.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.30, PDF p. 28, equations (121), (122), (123), (124), (125).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.30 Strategy: Short call synthetic straddle This sideways strategy (which is the same as a short straddle with the put replaced by a synthetic put) amounts to buying stock and selling two ATM (or the nearest 24 Similarly to long guts, here we assume that C > K2 − K1 . 25 Academic literature on synthetic straddles appears to be scarce. See, e.g., [Trifonov et al, 2011], [Trifonov et al, 2014]. 28 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur. All Rights Reserved. OTM) call options with a strike price K. The trader’s outlook is neutral. This is a capital gain strategy. We have (assuming S0 ≤ K): fT = ST − S0 − 2 × (ST − K)+ + C (121) S∗up = 2 × K − S0 + C (122) S∗down = S0 − C (123) Pmax = K − S0 + C (124) Lmax = unlimited (125)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.30"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.30 Strategy: Short call synthetic straddle This sideways strategy (which is the same as a short straddle with the put replaced by a synthetic put) amounts to buying stock and selling two ATM (or the nearest 24 Similarly to long guts, here we assume that C > K2 − K1 . 25 Academic literature on synthetic straddles appears to be scarce. See, e.g., [Trifonov et al, 2011], [Trifonov et al, 2014]. 28 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur. All Rights Reserved. OTM) call options with a strike price K. The trader’s outlook is neutral. This is a capital gain strategy. We have (assuming S0 ≤ K): fT = ST − S0 − 2 × (ST − K)+ + C (121) S∗up = 2 × K − S0 + C (122) S∗down = S0 − C (123) Pmax = K − S0 + C (124) Lmax = unlimited (125)"


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
