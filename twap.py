import time
def twap_order(client, symbol, side, total_quantity, intervals, delay_seconds):
    qty_per_order = total_quantity / intervals
    for _ in range(intervals):
        client.futures_create_order(
            symbol=symbol, side=side,
            type="MARKET", quantity=round(qty_per_order, 3)
        )
        time.sleep(delay_seconds)
