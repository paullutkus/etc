
import sys
import socket
import json

"""
This is a method to calculate the fair value of the ETF and then output an order based on the current
price
"""

def etf_trade_mean(fair_value_book, key):
    return fair_value_book["key"][0]

def calculate_ETF_order_type(fair_value_book, positions):
    if fair_value_book["XLF"][1] < 25:
        return None
    conversion_cost = 100
    ETF_MEAN = etf_trade_mean(fair_value_book, "XLF")
    WFC_MEAN = etf_trade_mean(fair_value_book, "WFC")
    GS_MEAN = etf_trade_mean(fair_value_book, "GS")
    MS_MEAN = etf_trade_mean(fair_value_book, "MS")
    BOND_FAIR = 300
    if 10 * ETF_MEAN + conversion_cost < BOND_FAIR + 2 * WFC_MEAN + 3 * MS_MEAN + 2*GS_MEAN:
        can_trade = can_trade_be_done(positions, "BUY_XLF")
        if can_trade:
            actions = [
                {"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "SELL", "price": BOND_FAIR + 1, "size": 30},
                {"type": "add", "order_id": order_id, "symbol": "GS", "dir": "SELL", "price": GS_MEAN + 1, "size": 20},
                {"type": "add", "order_id": order_id, "symbol": "MS", "dir": "SELL", "price": MS_MEAN + 1, "size": 30},
                {"type": "add", "order_id": order_id, "symbol": "WFC", "dir": "SELL", "price": WFC_MEAN + 1, "size": 20},
                {"type": "add", "order_id": order_id, "symbol": "GS", "dir": "SELL", "price": GS_MEAN + 1, "size": 20},
                {"type": "add", "order_id": order_id, "symbol": "XLF", "dir": "BUY", "price": ETF_MEAN - 1, "size": 100},
            ]
        else:
            return None
    elif 10 * ETF_MEAN + conversion_cost > BOND_FAIR + 2 * WFC_MEAN + 3 * MS_MEAN + 2*GS_MEAN:
        can_trade = can_trade_be_done(positions, "SELL_XLF")
        if can_trade:
            actions = [
                {"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "BUY", "price": BOND_FAIR - 1, "size": 30},
                {"type": "add", "order_id": order_id, "symbol": "GS", "dir": "BUY", "price": GS_MEAN - 1, "size": 20},
                {"type": "add", "order_id": order_id, "symbol": "MS", "dir": "BUY", "price": MS_MEAN - 1, "size": 30},
                {"type": "add", "order_id": order_id, "symbol": "WFC", "dir": "BUY", "price": WFC_MEAN - 1, "size": 20},
                {"type": "add", "order_id": order_id, "symbol": "GS", "dir": "BUY", "price": GS_MEAN - 1, "size": 20},
                {"type": "add", "order_id": order_id, "symbol": "XLF", "dir": "SELL", "price": ETF_MEAN + 1, "size": 100}
            ]
        else:
            return None

def can_trade_be_done(positions, type_of_trade):
    if type_of_trade == "BUY_XLF":
        if positions["XLF"] >= 0 and positions["GS"] <= 80 and positions["MS"] <= 80 and positions["BOND"] <= 70 and positions["WFC"] <= 80:
            return True
        return False
    else:
        if positions["XLF"] <= 0 and positions["GS"] >= -80 and positions["MS"] >= -80 and positions["BOND"] >= -70 and positions["WFC"] >= -80:
            return True
        return False



