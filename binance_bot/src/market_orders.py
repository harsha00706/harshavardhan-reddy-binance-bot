import sys
import logging
import os
from binance import Client

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")
if not API_KEY or not API_SECRET:
    raise RuntimeError("API keys not found in environment variables")

def place_market_order(symbol, side, quantity):
    client = Client(API_KEY, API_SECRET, testnet=True)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
    print("PING:", client.futures_ping())
    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )

    logging.info(f"MARKET ORDER: {order}")
    print(order)
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python src/market_orders.py BTCUSDT BUY 0.01")
        sys.exit(1)
    _, symbol, side, qty = sys.argv
    place_market_order(symbol, side, qty)

