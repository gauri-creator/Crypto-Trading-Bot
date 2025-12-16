import sys
from binance.client import Client
from config import API_KEY, API_SECRET
from logger import logger
from utils import validate_symbol, validate_quantity

client = Client(API_KEY, API_SECRET)

def place_market_order(symbol, side, quantity):
    validate_symbol(symbol)
    validate_quantity(quantity)
    order = client.futures_create_order(
        symbol=symbol, side=side, type="MARKET", quantity=quantity
    )
    logger.info(f"Market order placed: {order}")
    print(order)

if __name__ == "__main__":
    _, symbol, side, qty = sys.argv
    place_market_order(symbol, side, qty)
