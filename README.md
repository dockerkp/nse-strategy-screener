# NSE Strategy Screener and 151 Trading Strategies Library

This repository implements every strategy heading in Kakushadze & Serur, including named variants and §3.10: **174 strategy modules**. One strategy lives in each module, grouped by the book's actual asset-class chapters.

## Structure

- `cash/`: 5 strategy modules
- `commodities/`: 6 strategy modules
- `convertibles/`: 2 strategy modules
- `cryptocurrencies/`: 2 strategy modules
- `distressed_assets/`: 7 strategy modules
- `etfs/`: 8 strategy modules
- `fixed_income/`: 15 strategy modules
- `futures/`: 7 strategy modules
- `fx/`: 6 strategy modules
- `global_macro/`: 4 strategy modules
- `indexes/`: 5 strategy modules
- `miscellaneous_assets/`: 4 strategy modules
- `options/`: 58 strategy modules
- `real_estate/`: 8 strategy modules
- `stocks/`: 21 strategy modules
- `structured_assets/`: 6 strategy modules
- `tax_arbitrage/`: 3 strategy modules
- `volatility/`: 7 strategy modules

Each asset folder also contains `__init__.py`; those package markers are not counted as strategies. Modules declare `STATUS`, `DATA_REQUIREMENTS`, `SIGNAL_RULE`, and a stable `signal(inputs)` adapter. Reference-only strategies explicitly wait for the named feed instead of inventing data or trades.

## NSE daily engine

The executable daily OHLCV helpers remain wired into `main.py` and `daily_picks.py` through the `stocks` package: price momentum, moving averages, low volatility, pairs/mean reversion, support/resistance (including Camarilla), channel/Donchian, KNN, and the strict 52-week SMA helper.

```bash
pip install -r requirements.txt
python main.py --output-dir output
python daily_picks.py --output output/daily_top10.csv
```

Yahoo Finance is a convenient research source, not an exchange-licensed real-time feed. Outputs are mechanical research screens, not investment advice.
