import sys
import socket
import json

"""
Method evaluates bond order based on price. Returns a json
order to execute
"""
def evaluate_bond_order(book, order_id):
    if book['BOND'][0] == 0:
        return {"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "BUY", "price": 999, "size": 100}
    if book['BOND'][1] == 0:
        return {"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "BUY", "price": 1001, "size": 100}
    buy_price = book['BOND'][0][0]
    sell_price = book['BOND'][1][0]
    book_buy_size, book_sale_size = calculate_positions(positions)
    if sell_price > 1000:
       return {"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "SELL", "price": sell_price, "size": book_buy_size}
    if buy_price < 1000:
        return {"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "BUY", "price": buy_price, "size": book_sale_size}
    else:
        return None

def balance_fill(filL_order):
   if message["type"] == "FILL":
    security_order = message["symbol"]
    if security_order == "BOND":
       if message["dir"] == "BUY":
            return {"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "SELL", "price": 1001, "size": message["size"]}
       else:
            return {"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "BUY", "price": 999, "size": message["size"]}

def calculate_positions(positions, trade):
    if positions["BOND"] == 0:
        return 100, 100
    else:
        if positions["BOND"] > 0:
            return 0, positions["BOND"]
        else:
            return positions["BOND"], 0