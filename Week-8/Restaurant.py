"""Restaurant"""
def main(price, promo, percent, food):
    """ Check Promotion """
    old_price = price
    if price >= promo:
        old_price = price - (price * percent / 100)
    new_price = (price + food) - ((price + food) * percent / 100)
    # check
    if old_price > new_price:
        print("Yes %.3f" % (abs(new_price - old_price)))
    elif old_price < new_price:
        print("No %.3f" % (abs(new_price - old_price)))
    else: # old_price == new_price
        print("Yes")

main(float(input()), float(input()), float(input()), float(input()))
