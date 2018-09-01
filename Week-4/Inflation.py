"""
Inflation
Author : Chanwit Settavongsin
"""
def main(price, year):
    """ Find Price in Future """
    price = int(price * 100)
    for _ in range(year):
        price += int((price * 381) // 10000)
    print("%i.%02i" % (price//100, price%100))

main(float(input()), int(input()))
