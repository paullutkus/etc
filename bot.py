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

# ~~~~~============== CONFIGURATION  ==============~~~~~
# replace REPLACEME with your team name!
team_name = "rector"
# This variable dictates whether or not the bot is connecting to the prod
# or test exchange. Be careful with this switch!
test_mode = True

# This setting changes which test exchange is connected to.
# 0 is prod-like
# 1 is slower
# 2 is empty
test_exchange_index = 2
prod_exchange_hostname = "production"

port = 25000 + (test_exchange_index if test_mode else 0)
exchange_hostname = "test-exch-" + team_name if test_mode else prod_exchange_hostname

book = {
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
    return msg

def pull_info_from_server(exchange):
    while True:
        message = read_from_exchange(exchange)
        if not message:
            print("Returned null")
            break
        if message["type"] == "close":
            print("The round has ended")
            break
        elif message["type"] == "book":
            book[message['symbol']] = (message['buy'], message['sell'])
        elif message["type"] == "trade":
            update_fair_value(message, fmv_book)

        trade_bond(book)

def update_positions(message):
    if not message["symbols"]:
        print("No position data")
    for security in message['symbols']:
         print(security)
         holding = security["position"]
         name = security["symbol"]
         positions[name] = holding





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
