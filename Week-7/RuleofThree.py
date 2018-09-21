"""
RuleofThree
Author : Chanwit Settavongsin
"""
def main(number, price_temp, weight_temp):
    """ find best value to buy snack """
    avg_temp = weight_temp / price_temp
    for _ in range(number - 1):
        price = float(input())
        weight = float(input())
        avg = weight / price
        if avg == avg_temp and price < price_temp:
            price_temp = price
            weight_temp = weight
            avg_temp = avg
        elif avg > avg_temp:
            price_temp = price
            weight_temp = weight
            avg_temp = avg
    print("%.2f %.2f" % (price_temp, weight_temp))

main(int(input()), float(input()), float(input()))
