"""Bearish short seagull spread.

Source: Kakushadze & Serur, 151 Trading Strategies, §2.56, PDF p. 38, equations (254), (255), (256), (257), (258), (259).
Status: REFERENCE_ONLY.
Data requirements: underlying prices, option quotes by strike/expiry, contract multipliers and rates.

Book rule summary: 2.56 Strategy: Bearish short seagull spread This option trading strategy is a bear put spread financed with a sale of an OTM call option. It amounts to a short position in an OTM put option with a strike price K1 , a long position in an ATM put option with a strike price K2 , and a short position in an OTM call option with a strike price K3 . Ideally, the trade should be structured to have zero cost. The trader’s outlook is bearish. This is a capital gain strategy. We have: fT = −(K1 − ST )+ + (K2 − ST )+ − (ST − K3 )+ − H (254) S∗ = K2 − H, H > 0 (255) S∗ = K3 − H, H < 0 (256) K2 ≤ S ∗ ≤ K3 , H = 0 (257) Pmax = K2 − K1 − H (258) Lmax = unlimited (259) 34 Academic literature on seagull spreads appears to be scarce. For a book reference, see, e.g., [Wystup, 2017]. 38 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur.
"""
from __future__ import annotations

from typing import Any, Mapping

SECTION = "2.56"
STATUS = "REFERENCE_ONLY"
DATA_REQUIREMENTS = "underlying prices, option quotes by strike/expiry, contract multipliers and rates"
SIGNAL_RULE = "2.56 Strategy: Bearish short seagull spread This option trading strategy is a bear put spread financed with a sale of an OTM call option. It amounts to a short position in an OTM put option with a strike price K1 , a long position in an ATM put option with a strike price K2 , and a short position in an OTM call option with a strike price K3 . Ideally, the trade should be structured to have zero cost. The trader’s outlook is bearish. This is a capital gain strategy. We have: fT = −(K1 − ST )+ + (K2 − ST )+ − (ST − K3 )+ − H (254) S∗ = K2 − H, H > 0 (255) S∗ = K3 − H, H < 0 (256) K2 ≤ S ∗ ≤ K3 , H = 0 (257) Pmax = K2 − K1 − H (258) Lmax = unlimited (259) 34 Academic literature on seagull spreads appears to be scarce. For a book reference, see, e.g., [Wystup, 2017]. 38 Electronic copy available at: https://ssrn.com/abstract=3247865 Copyright c 2018 Zura Kakushadze and Juan Andrés Serur."


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
