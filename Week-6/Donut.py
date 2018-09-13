"""
Donut
Author : Chanwit Settavongsin
"""
def main(price, buy_promo, free_promo, want):
    """
    Get optimal way to buy donut
    input : price = donut price
            buy_promo = promotion
            free_promo = free donut
            want = donut require
    output : price to pay, total of donut
    """
    box = buy_promo + free_promo # total in one box
    buybox = want // box # number of box to buy
    missing = want - (buybox * box) # number of missing to buy
    if missing >= buy_promo:
        buybox += 1
        missing = 0
    pay = ((buybox * buy_promo) + missing) * price
    get = box * buybox + missing
    print(pay, get)

main(int(input()), int(input()), int(input()), int(input()))
