"""Donchian channel signals from §3.15 of 151 Trading Strategies."""
from __future__ import annotations

import pandas as pd


def donchian_state(daily: pd.DataFrame, lookback: int = 20) -> int:
    """Return +1 above the prior high, -1 below the prior low, else 0."""
        if len(daily) < lookback + 1:
                return 0
                    current = float(daily["Close"].iloc[-1])
                        prior = daily.iloc[-lookback - 1:-1]
                            if current > float(prior["High"].max()):
                                    return 1
                                        if current < float(prior["Low"].min()):
                                                return -1
                                                    return 0


                                                    def donchian_breakout(daily: pd.DataFrame, lookback: int = 20) -> int:
                                                        """Follow a channel breakout (+1 up, -1 down), as noted in §3.15.

                                                            Experimental: §3.15 also discusses contrarian use and does not fully specify
                                                                execution, exits, or the channel length. This function supplies only state.
                                                                    """
                                                                        return donchian_state(daily, lookback=lookback)


                                                                        def donchian_contrarian(daily: pd.DataFrame, lookback: int = 20) -> int:
                                                                            """Fade the same channel break; the sign is opposite the breakout state."""
                                                                                return -donchian_state(daily, lookback=lookback)
                                                                                