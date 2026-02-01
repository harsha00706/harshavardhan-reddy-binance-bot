# Binance Futures Trading Bot (Testnet)

## Overview
This project is a Python-based command-line trading bot built using the Binance USDT-M Futures Testnet API.
It supports both basic and advanced order types, includes robust input validation, structured logging,
and demonstrates practical trading logic aligned with real-world futures trading systems.

The bot is modular, testnet-safe, and designed to meet professional coding and evaluation standards
for a junior Python developer role.

## Key Features

### Core Functionality
- Market orders (Buy / Sell)
- Limit orders
- Binance Futures Testnet integration
- Command-line interface (CLI)
- Secure API key handling using environment variables
- Input validation (symbol, quantity, price thresholds)
- Structured logging (bot.log)
- Error handling and traceability

### Advanced Trading Features
- Stop-Market Orders (Stop-Loss / Breakout entries)
- Simulated OCO (One-Cancels-the-Other) orders for Futures
- TWAP (Time-Weighted Average Price) execution
- Grid trading strategy

Note: Binance Futures does not provide native OCO orders.
OCO is implemented by combining a LIMIT take-profit order with a STOP-MARKET stop-loss order
and canceling the remaining order once one is executed.

## Project Structure

binance_bot/
├── src/
│   ├── market_orders.py
│   ├── limit_orders.py
│   └── advanced/
│       ├── stop_limit.py
│       ├── oco.py
│       ├── twap.py
│       └── grid.py
├── bot.log
└── README.md

## Requirements
- Python 3.9+
- python-binance library
- Binance Futures Testnet API key

Install dependencies:
pip install python-binance

## API Configuration

API credentials are read securely from environment variables.

Windows (PowerShell):
$env:BINANCE_API_KEY="your_testnet_api_key"
$env:BINANCE_API_SECRET="your_testnet_api_secret"

Linux / macOS:
export BINANCE_API_KEY="your_testnet_api_key"
export BINANCE_API_SECRET="your_testnet_api_secret"

API Key Requirements:
- Enable Reading
- Enable Futures
- Restrict access to trusted IPs

## Usage (CLI Commands)

Market Order:
python src/market_orders.py BTCUSDT BUY 0.01
python src/market_orders.py BTCUSDT SELL 0.01

Limit Order:
python src/limit_orders.py BTCUSDT BUY 0.01 85000
python src/limit_orders.py BTCUSDT SELL 0.01 90000

Stop-Market Order:
python src/advanced/stop_limit.py BTCUSDT SELL 0.01 86000
python src/advanced/stop_limit.py BTCUSDT BUY 0.01 89000

OCO (Simulated):
python src/advanced/oco.py BTCUSDT SELL 0.01 90000 86000

TWAP:
python src/advanced/twap.py BTCUSDT BUY 0.05 5

Grid Trading:
python src/advanced/grid.py BTCUSDT BUY 84000 92000 5 0.01

## Logging

All actions are recorded in bot.log:
- Order requests
- Executions
- Strategy steps
- Errors

Sample log entry:
2026-01-01 18:12:03 | INFO | MARKET ORDER REQUEST | Symbol=BTCUSDT Side=BUY Qty=0.01

## Technical Notes
- Futures endpoint: https://testnet.binancefuture.com/fapi
- STOP_MARKET orders are used for reliability on Futures Testnet
- OCO implemented via monitoring and cancellation logic
- TWAP and Grid demonstrate algorithmic trading concepts

## Disclaimer
This project uses Binance Futures Testnet only.
No real funds are involved. This project is intended for educational and evaluation purposes only.

## Author
Harshavardhan Reddy
Python Developer – Binance Future Orders Bot


