import os
import sys
import time
import logging
from binance import Client

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

def twap(symbol, side, total_qty, slices):
    client = Client(API_KEY, API_SECRET, testnet=True)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    qty_per_slice = round(float(total_qty) / int(slices), 6)

    logging.info(
        f"TWAP STARTED | Symbol={symbol} Side={side} "
        f"TotalQty={total_qty} Slices={slices}"
    )

    for i in range(int(slices)):
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=qty_per_slice
        )

        logging.info(
            f"TWAP SLICE EXECUTED | Slice={i+1}/{slices} "
            f"OrderID={order['orderId']} Qty={qty_per_slice}"
        )

        print(f"Slice {i+1}/{slices} executed")
        time.sleep(5)

    logging.info("TWAP COMPLETED")

if __name__ == "__main__":
    _, sym, side, qty, parts = sys.argv
    twap(sym, side, qty, parts)
