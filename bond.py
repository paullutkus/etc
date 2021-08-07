

def trade_bond(book):
    if book['BOND'][0] > 1000:
       return f'ADD 1 BOND SELL {book['BOND'][0] 1}'
    elif book['BOND'][1] < 1000:
       return f'ADD 1 BOND BUY {book['BOND'][1] 1}'


