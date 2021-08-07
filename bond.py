

def trade_bond(book, order_id):
    #print(book['BOND'])
    if book['BOND'][0] == 0:
        buy = "ADD " + str(order_id) + "BOND BUY 5 999"
        return buy
    elif book['BOND'][1] == 0:
        sell = "ADD " + str(order_id) + "BOND SELL 5 1001"
        return sell
 
    elif book['BOND'][1][0] > 1000:
        sell = "ADD " + str(order_id) + " BOND SELL " + str(book['BOND'][1][0]) + " " + str(book['BOND'][1][1]) 
        #print(sell)
        
        return sell
    elif book['BOND'][0][0] < 1000:
        #print("hi ", book['BOND'])
        buy = "ADD " + str(order_id) + " BOND BUY " + str(book['BOND'][0][0]) + " " + str(book['BOND'][0][1])  
        #print("bond buy:", book['BOND'][0]) 
        #buy = " " 
        #print(buy)
        
        return buy 
    else:
        return None

