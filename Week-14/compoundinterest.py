"""
compoundinterest
Author : Chanwit Settavongsin
"""
def main(money, interest, year):
    """ Find money with Compound Interest """
    for _ in range(year):
        money = money + (money * interest / 100)
    print("%.s2f" % (money))

main(int(input()), float(input()), int(input()))
