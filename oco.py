def place_oco(client, symbol, side, take_profit_price, stop_loss_price):
    tp = client.futures_create_order(
        symbol=symbol, side=side,
        type="TAKE_PROFIT_MARKET",
        stopPrice=take_profit_price, closePosition=True
    )
    sl = client.futures_create_order(
        symbol=symbol, side=side,
        type="STOP_MARKET",
        stopPrice=stop_loss_price, closePosition=True
    )
    return {"take_profit": tp, "stop_loss": sl}
