import os
import sys
import logging
from binance import Client
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")
logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
def place_limit_order(symbol, side, quantity, price, api_key, api_secret):
    client = Client(API_KEY, API_SECRET, testnet=True)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )
        logging.info(f"LIMIT ORDER: {order}")
        print(order)
    except Exception as e:
        logging.error(f"LIMIT ORDER FAILED: {e}")
        print("Error:", e)
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python src/limit_orders.py BTCUSDT SELL 0.01 65000 API_KEY API_SECRET")
        sys.exit(1)
    _, symbol, side, qty, price = sys.argv
    place_limit_order(symbol, side, qty, price, API_KEY, API_SECRET)
