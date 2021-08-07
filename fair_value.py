
def update_fair_value(trade, fmv_book):

        fmv_book[trade["symbol"]][0] = calc_fair_value(fmv_book[trade["symbol"]][0], fmv_book[trade["symbol"]][1], trade["price"], trade["size"])

        fmv_book[trade["symbol"]][1] += trade["size"]
       # fmv_book[trade["symbol"]][1] += 1



def init_fair_value(book):
    fmv_book = {}
    for key in book:
        fmv_book[key] = [0,0]
    return fmv_book

# def active_fair_values(fmv_book):
#     print(  )

def calc_fair_value(average, size, new_price, trade_size):
    #new_average = average + (new_price - average) / (size + 1)
    new_average = (size * average + new_price * trade_size) / (size + trade_size)
    return new_average

    #if trade_size == 1:
    #return new_average
    #else:
    #return new_average + calc_fair_value(average, size + 1, new_price, trade_size - 1)

