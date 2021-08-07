import sys
import socket
import json

"""
Method evaluates bond order based on price. Returns a json
order to execute
"""
def evaluate_bond_order(book, order_id, positions):
    if book['BOND'][0] == 0:
        return {"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "BUY", "price": 999, "size": 1}
    if book['BOND'][1] == 0:
        return {"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "BUY", "price": 1001, "size": 1}
    buy_price = book['BOND'][0][0]
    sell_price = book['BOND'][1][0]
    book_buy_size, book_sale_size = calculate_positions(positions)
    if sell_price > 1000:
       return {"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "SELL", "price": sell_price, "size": 1}
    if buy_price < 1000:
        return {"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "BUY", "price": buy_price, "size": 1}
    else:
        return None

def balance_fill(fmv_book, fill_order, order_id):
    security_order = fill_order["symbol"]
    if security_order == "BOND":
       if fill_order["dir"] == "BUY":
            return {"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "SELL", "price": 1001, "size": fill_order["size"]}
       else:
            return {"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "BUY", "price": 999, "size": fill_order["size"]}
    else:
        if fill_order["dir"] == "BUY":
            return {"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "SELL", "price": fmv_book[security_order] + 1, "size": fill_order["size"]}
       else:
            return {"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "BUY", "price": fmv_book[security_order] - 1, "size": fill_order["size"]}

def calculate_positions(positions):
    if positions["BOND"] == 0:
        return 100, 100
    else:
        if positions["BOND"] > 0:
            return 0, positions["BOND"]
        else:
            return positions["BOND"], 0
