import os
import sys
import logging
import numpy as np
from binance import Client

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

def grid_trade(symbol, side, lower, upper, grids, qty):
    client = Client(API_KEY, API_SECRET, testnet=True)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    prices = np.linspace(float(lower), float(upper), int(grids))

    logging.info(
        f"GRID STARTED | Symbol={symbol} Side={side} "
        f"Range={lower}-{upper} Grids={grids} Qty={qty}"
    )

    for price in prices:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            price=round(price, 2),
            quantity=qty,
            timeInForce="GTC"
        )

        logging.info(
            f"GRID ORDER PLACED | "
            f"OrderID={order['orderId']} "
            f"Price={price} Qty={qty}"
        )

        print(f"Grid order placed at {price}")

    logging.info("GRID COMPLETED")

if __name__ == "__main__":
    _, sym, side, low, high, grids, qty = sys.argv
    grid_trade(sym, side, low, high, grids, qty)
