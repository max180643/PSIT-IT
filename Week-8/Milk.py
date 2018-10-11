"""
Milk
Author : Chanwit Settavongsin
"""
def main(price, promo, free, money):
    """ The amount of milk to be taken."""
    milk, caps = money // price, money // price
    while caps >= promo and promo != 0:
        get = free * (caps // promo)
        caps = caps % promo + get
        milk += get
    print(milk)

main(int(input()), int(input()), int(input()), int(input()))
