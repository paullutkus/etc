import pandas as pd


def update_fair_value(trade, fmv_book):

    for i in range(trade["size"]):
        fmv_book[trade["symbol"]] = fmv_book[trade["symbol"]].append({key : trade["price"]}, ignore_index=True)


        # fmv_book[trade["symbol"]][0] = calc_fair_value(fmv_book[trade["symbol"]][0], fmv_book[trade["symbol"]][1], trade["price"], trade["size"])

        # fmv_book[trade["symbol"]][1] += trade["size"]
       # fmv_book[trade["symbol"]][1] += 1



def init_fair_value(book):
    fmv_book = {}
    for key in book:
        fmv_book[key] = pd.DataFrame(columns = [key])

    return fmv_book

def place_fmv_order(book, key, value):

    if(key == "VALBZ" or key == "VALE"):
        buy = {"type": "add", "order_id": 1, "symbol": key, "dir": "BUY", "price": value - 1, "size": 10}

        sell = {"type": "add", "order_id": 2, "symbol": key, "dir": "BUY", "price": value + 1, "size": 10}
    else:
        buy = {"type": "add", "order_id": 1, "symbol": key, "dir": "BUY", "price": value - 1, "size": 100}

        sell = {"type": "add", "order_id": 2, "symbol": key, "dir": "BUY", "price": value + 1, "size": 100}

    return buy, sell

def fmv_book_ready(book):
    for key in book:
        if(book[key].size < 100):
            return False
    return True



def calc_fair_value(average, size, new_price, trade_size):
    #new_average = average + (new_price - average) / (size + 1)
    new_average = (size * average + new_price * trade_size) / (size + trade_size)
    return new_average

    #if trade_size == 1:
    #return new_average
    #else:
    #return new_average + calc_fair_value(average, size + 1, new_price, trade_size - 1)

