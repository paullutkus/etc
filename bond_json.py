import sys
import socket
import json

"""
Method evaluates bond order based on price. Returns a json
order to execute
"""
def evaluate_bond_order(buy_price, sell_price, order_id, book_buy_size, book_sale_size):
    if buy_price is None:
        return {"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "BUY", "price": 999, "size": 5}
    elif sell_price is None:
        return {"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "BUY", "price": 1001, "size": 5}
    if sell_price > 1000
       return {"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "SELL", "price": sell_price, "size": book_buy_size}
    if buy_price < 1000:
        return {"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "BUY", "price": buy_price, "size": book_sale_size}
    else:
        return None

