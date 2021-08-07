def update_fair_value(average, size, new_price):
    return (size * average + new_price) / (size + 1)