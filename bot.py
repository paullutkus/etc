#!/usr/bin/python
# ~~~~~==============   HOW TO RUN   ==============~~~~~
# 1) Configure things in CONFIGURATION section
# 2) Change permissions: chmod +x bot.py
# 3) Run in loop: while true; do ./bot.py; sleep 1; done

from __future__ import print_function

import sys
import socket
import json
from bond import trade_bond
from fair_value import calc_fair_value, init_fair_value, update_fair_value
from bond_json import evaluate_bond_order, balance_fill


# ~~~~~============== CONFIGURATION  ==============~~~~~
# replace REPLACEME with your team name!
team_name = "rector"
# This variable dictates whether or not the bot is connecting to the prod
# or test exchange. Be careful with this switch!
test_mode = False

# This setting changes which test exchange is connected to.
# 0 is prod-like
# 1 is slower
# 2 is empty
test_exchange_index = 1
prod_exchange_hostname = "production"

port = 25000 + (test_exchange_index if test_mode else 0)
exchange_hostname = "test-exch-" + team_name if test_mode else prod_exchange_hostname

order_id = 0

book = {
    'BOND': [0, 0],
    'GS': [0, 0],
    'MS': [0, 0],
    'VALBZ': [0, 0], 
    'VALE': [0, 0], 
    'GS': [0, 0],
    'MS': [0, 0],
    'WFC': [0, 0],
    'XLF': [0, 0],
}



filled_orders = {}

positions={
    'BOND': 0,
    'GS': 0,
    'MS': 0,
    'VALBZ': 0,
    'VALE': 0,
    'GS': 0,
    'MS': 0,
    'WFC': 0,
    'XLF': 0,
}

fmv_book = init_fair_value(book)

# ~~~~~============== NETWORKING CODE ==============~~~~~
def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((exchange_hostname, port))
    return s.makefile("rw", 1)


def write_to_exchange(exchange, obj):
    json.dump(obj, exchange)
    exchange.write("\n")


def read_from_exchange(exchange):
    msg = json.loads(exchange.readline())
    update_positions(msg)

    update_our_positions(msg)


    return msg

def buy_num(sym, num):
    return {"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "BUY", "price": 999, "size": 1}
  

def pull_info_from_server(exchange):
    

    buy = {"type": "add", "order_id": 1, "symbol": "BOND", "dir": "BUY", "price": 999, "size": 100}

    write_to_exchange(exchange, buy)

    sell = {"type": "add", "order_id": 2, "symbol": "BOND", "dir": "BUY", "price": 1001, "size": 100}

    write_to_exchange(exchange, sell)

    order_id = 3

    while True:
        message = read_from_exchange(exchange)
        if not message:
            print("Returned null")
            break
        elif message["type"] == "fill" or message["type"] == "reject" or message["type"] == "ack":
            print(message)
        if message["type"] == "close":
            print("The round has ended")
            break
        elif message["type"] == "fill":
            trade = balance_fill(message, order_id)
            order_id += 1
            write_to_exchange(exchange, trade)
            
        elif message["type"] == "book":
            update_book(message)

        # order_id += 1

        # bond = evaluate_bond_order(book, order_id, positions)
        # #update_fair_value(bond, fmv_book)
        # #print(bond)
        # bond_test =  
        # if not bond:
        #     print("Bond was null")
        #     continue
        # elif order_id % 3 == 0:
        #     write_to_exchange(exchange, bond)

def update_positions(message):
    if message["type"] == "hello":
        if not message["symbols"]:
             print("No position data")
        for security in message['symbols']:
             #print(security)
             holding = security["position"]
             name = security["symbol"]
             positions[name] = holding

def update_book(message):
    sym = message["symbol"]
    book[sym][0] = message["buy"]
    book[sym][1] = message["sell"]
    print(sym, book[sym])

def update_our_positions(message):
    if message["type"] == "FILL":
        #Keep Track of our orders
        order_id_fill = message["order_id"]
        #open_orders[order_id_fill] = None
        filled_orders[order_id_fill] = True

        #Keep track of our positions
        security_order = message["symbol"]
        size_of_order = message["price"]
        type_of_message = message["dir"]

        if type_of_message == "SELL":
            size_of_order *= -1
        positions[security_order] -= size_of_order





# ~~~~~============== MAIN LOOP ==============~~~~~


def main():
    exchange = connect()
    write_to_exchange(exchange, {"type": "hello", "team": team_name.upper()})
    hello_from_exchange = read_from_exchange(exchange)
    print("positions", positions)
    # A common mistake people make is to call write_to_exchange() > 1
    # time for every read_from_exchange() response.
    # Since many write messages generate marketdata, this will cause an
    # exponential explosion in pending messages. Please, don't do that!
    print("The exchange replied:", hello_from_exchange, file=sys.stderr)


    pull_info_from_server(exchange)


        
if __name__ == "__main__":
    main()
