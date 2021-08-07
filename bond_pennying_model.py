
import sys
import socket
import json

"""
Method evaluates bond order based on price. Returns a json
order to execute 
"""
def evaluate_bond_order(price, order_id, book_size):
    if price == 1001:
       return {"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "SELL", "price": price, "size": book_size}
    elif price == 999:
        return {"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "BUY", "price": price, "size": book_size}
    else:
        return None