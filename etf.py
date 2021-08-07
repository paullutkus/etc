
import sys
import socket
import json

"""
This is a method to calculate the fair value of the ETF and then output an order based on the current
price
"""

spread = 50

def etf_trade_mean(fair_value_book, key):
    return fair_value_book["key"][0]/fair_value_book["key"][1]

def calculate_ETF_order_type(fair_value_book, trade_log_book):
    etf_trade_mean = 150
    WFC_MEAN = etf_trade_mean(fair_value_book, "WFC")
    GS_MEAN = etf_trade_mean(fair_value_book, "GS")
    MS_MEAN = etf_trade_mean(fair_value_book, "MS")
    BOND_FAIR = 300

    if 10 * etf_trade_mean + spread < BOND_FAIR + 2 * WFC_MEAN + 3 * MS_MEAN + 2*GS_MEAN:
        #return a sell
    elif  10 * etf_trade_mean - spread > BOND_FAIR + 2 * WFC_MEAN + 3 * MS_MEAN + 2*GS_MEAN:
        #return a buy


def penny_ETF():


