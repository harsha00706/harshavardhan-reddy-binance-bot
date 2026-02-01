import os
import sys
import logging
from binance import Client

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

def place_stop_market(symbol, side, quantity, stop_price):
    client = Client(API_KEY, API_SECRET, testnet=True)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    logging.info(
        f"STOP-MARKET ORDER REQUEST | Symbol={symbol} Side={side} Qty={quantity} StopPrice={stop_price}"
    )

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="STOP_MARKET",
        stopPrice=stop_price,
        quantity=quantity
    )

    logging.info(f"STOP-MARKET ORDER SUCCESS | {order}")
    print(order)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python stop_limit.py SYMBOL SIDE QTY STOP_PRICE")
        sys.exit(1)

    _, sym, side, qty, stop_p = sys.argv
    place_stop_market(sym, side, qty, stop_p)
