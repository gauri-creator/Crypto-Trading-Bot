def place_stop_limit(client, symbol, side, quantity, stop_price, limit_price):
    return client.futures_create_order(
        symbol=symbol, side=side, type="STOP",
        quantity=quantity, price=limit_price,
        stopPrice=stop_price, timeInForce="GTC"
    )
