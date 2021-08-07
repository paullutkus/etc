

def trade_bond(book):
    if book['BOND'][0] > 1000:
       return "ADD 1 BOND SELL %d 1"(book['BOND'][0])
    elif book['BOND'][1] < 1000:
       return "ADD 1 BOND BUY %d 1"(book['BOND'][1]) 


