
def update_fair_value(trade, fmv_book):
        fmv_book[trade["symbol"]][1] += 1
        fmv_book[trade["symbol"]][0] = calc_fair_value(fmv_book[trade["symbol"]][0], fmv_book[trade["symbol"]][1], trade["price"])



def init_fair_value(book):
    fmv_book = {}
    for key in book:
        fmv_book[key] = (0,0)
    return fmv_book


def calc_fair_value(average, size, new_price):
    return average + ((new_price - average) / size)