import sys
import socket
import json

"""
Method evaluates bond order based on price. Returns a json
order to execute
"""
def evaluate_bond_order(book, order_id):
    if book['BOND'][0] == 0:
        return {"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "BUY", "price": 999, "size": 5}
    if book['BOND'][1] == 0:
        return {"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "BUY", "price": 1001, "size": 5}
    buy_price = book['BOND'][0][0]
    sell_price = book['BOND'][1][0]
    book_buy_size = book['BOND'][0][1]
    book_sale_size = book['BOND'][1][1]
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

