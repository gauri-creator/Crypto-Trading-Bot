def grid_strategy(client, symbol, quantity, lower_price, upper_price, grids):
    step = (upper_price - lower_price) / grids
    for i in range(grids):
        buy_price = round(lower_price + i * step, 2)
        sell_price = round(buy_price + step, 2)
        client.futures_create_order(
            symbol=symbol, side="BUY", type="LIMIT",
            quantity=quantity, price=buy_price, timeInForce="GTC"
        )
        client.futures_create_order(
            symbol=symbol, side="SELL", type="LIMIT",
            quantity=quantity, price=sell_price, timeInForce="GTC"
        )
