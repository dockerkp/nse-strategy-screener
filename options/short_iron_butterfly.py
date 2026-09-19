"""“Short” iron butterfly.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.45, PDF p. 34, equations (201), (202), (203), (204), (205).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.45 Strategy: “Short” iron butterfly This volatility strategy is a combination of a bear put spread and a bull call spread and consists of a short position in an OTM put option with a strike price K1 , a long position in an ATM put option and an ATM call option with a strike price K2 , and a short position in an OTM call option with a strike price K3 . The strikes are equidistant: K2 − K1 = K3 − K2 = κ. This is a net debit trade. The trader’s outlook is neutral. This is a capital gain strategy. We have: fT = (K2 − ST )+ + (ST − K2 )+ − (K1 − ST )+ − (ST − K3 )+ − D (201) S∗up = K2 + D (202) S∗down = K2 − D (203) Pmax = κ − D (204) Lmax = D (205)
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.45"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.45 Strategy: “Short” iron butterfly This volatility strategy is a combination of a bear put spread and a bull call spread and consists of a short position in an OTM put option with a strike price K1 , a long position in an ATM put option and an ATM call option with a strike price K2 , and a short position in an OTM call option with a strike price K3 . The strikes are equidistant: K2 − K1 = K3 − K2 = κ. This is a net debit trade. The trader’s outlook is neutral. This is a capital gain strategy. We have: fT = (K2 − ST )+ + (ST − K2 )+ − (K1 − ST )+ − (ST − K3 )+ − D (201) S∗up = K2 + D (202) S∗down = K2 − D (203) Pmax = κ − D (204) Lmax = D (205)"


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
