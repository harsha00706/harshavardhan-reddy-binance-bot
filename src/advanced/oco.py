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

def simulate_oco(symbol, side, qty, take_profit, stop_loss):
    client = Client(API_KEY, API_SECRET, testnet=True)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    logging.info(
        f"OCO STARTED | Symbol={symbol} Side={side} TP={take_profit} SL={stop_loss}"
    )

    # Take Profit (LIMIT)
    tp_order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        price=take_profit,
        quantity=qty,
        timeInForce="GTC"
    )

    # Stop Loss (STOP_MARKET)
    sl_order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="STOP_MARKET",
        stopPrice=stop_loss,
        closePosition=True
    )

    print("OCO simulation started")

    while True:
        open_orders = client.futures_get_open_orders(symbol=symbol)
        if len(open_orders) < 2:
            for o in open_orders:
                client.futures_cancel_order(
                    symbol=symbol,
                    orderId=o["orderId"]
                )
            logging.info("OCO COMPLETED | Remaining order cancelled")
            print("One order filled, other cancelled")
            break
        time.sleep(5)

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python oco.py SYMBOL SIDE QTY TAKE_PROFIT STOP_LOSS")
        sys.exit(1)

    _, sym, side, qty, tp, sl = sys.argv
    simulate_oco(sym, side, qty, tp, sl)
