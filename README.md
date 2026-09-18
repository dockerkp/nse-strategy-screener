# NSE Strategy Screener

A strict NSE equity screening pipeline that:

1. downloads the current NSE `EQ`-series equity universe;
2. keeps stocks whose latest close is above a 52-week simple moving average, requiring 52 valid weekly closes; and
3. calculates daily Camarilla H1-H4 and L1-L4 from the latest completed session's high, low and close.

The code is arranged so more daily-bar strategies can be added under `strategies/`.

## Data and limitations

- Universe: NSE's official equity list (`EQUITY_L.csv`), filtered to `SERIES == EQ`.
- Prices: Yahoo Finance via `yfinance`. Yahoo is convenient but is not an exchange-licensed real-time feed. Missing or stale symbols are reported, not silently filled.
- The screen uses completed daily bars. Standard daily Camarilla levels for a trading day use the previous completed session's H/L/C.
- Corporate actions, symbol mappings, illiquid stocks and Yahoo coverage can affect results.
- Outputs are mechanical research screens, not investment advice.

For licensed exchange-wide NSE snapshots, replace the downloader in `data.py` with a vendor adapter such as Global Datafeeds.

## Install

Python 3.11+ is recommended.

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## Run

```bash
python main.py --output-dir output
```

Useful options:

```bash
python main.py --help
python main.py --batch-size 100 --pause 1.0
python main.py --limit 50        # quick test only
```

Files written:

- `output/nse_52week_sma_screen.csv`
- `output/nse_daily_camarilla.csv`
- `output/coverage_report.csv`

`coverage_report.csv` makes gaps explicit. A symbol is only included in the SMA pass list when there are at least 52 valid weekly closes and the latest close is strictly greater than the 52-week SMA.

## Add a strategy

Create a module in `strategies/` that accepts one symbol's completed daily OHLCV DataFrame and returns signal fields. Register it in `strategies/__init__.py`. Keep strategy rules mechanical and make required data explicit.

## Camarilla formula

With `R = high - low`:

- `H1, H2, H3, H4 = close + R * 1.1 / (12, 6, 4, 2)`
- `L1, L2, L3, L4 = close - R * 1.1 / (12, 6, 4, 2)`

Formula reference: https://www.clientam.com.hk/en/software/tws/usersguidebook/technicalanalytics/camarillapivotpoints.htm

## Daily top-10 picks engine

Run after the previous NSE session has completed and before the next open:

```bash
python daily_picks.py --output output/daily_top10.csv
```

It combines the book's 12-1 momentum, 10/30 MA state, 3/10/21 MA state, classic pivot, low-volatility rank and Donchian state. It excludes histories whose latest bar does not match the modal latest NSE session. The output contains direction, next-session pivot entry trigger, R1/S1 target, and a 2% stop. The book does not prescribe a stop for most strategies; this shared 2% stop is a deliberate risk overlay based on the example in its two-moving-average section.

Entry triggers are levels, not guaranteed fills. A live or broker feed is required to determine whether a trigger traded and at what executable price.
