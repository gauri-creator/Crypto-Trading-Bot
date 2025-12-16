import sys
from binance.client import Client
from config import API_KEY, API_SECRET
from logger import logger
from utils import validate_symbol, validate_quantity, validate_price

client = Client(API_KEY, API_SECRET)

def place_limit_order(symbol, side, quantity, price):
    validate_symbol(symbol)
    validate_quantity(quantity)
    validate_price(price)
    order = client.futures_create_order(
        symbol=symbol, side=side, type="LIMIT",
        quantity=quantity, price=price, timeInForce="GTC"
    )
    logger.info(f"Limit order placed: {order}")
    print(order)

if __name__ == "__main__":
    _, symbol, side, qty, price = sys.argv
    place_limit_order(symbol, side, qty, price)
