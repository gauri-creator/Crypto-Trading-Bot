def validate_symbol(symbol):
    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT-M Futures symbols allowed")

def validate_quantity(qty):
    if float(qty) <= 0:
        raise ValueError("Quantity must be greater than zero")

def validate_price(price):
    if float(price) <= 0:
        raise ValueError("Price must be greater than zero")
