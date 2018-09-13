"""
[EX] Taxi v.1
Author : Chanwit Settavongsin
"""
from math import ceil, floor
def main(distance, jam_time, price):
    """ Calculate Taxi Price """
    # distance price calculate
    if distance != 0:
        for i in range(1, distance + 1):
            price += price_check(i)
    else:
        price += price_check(distance)
    if ceil(price) % 2 == 0:
        price = ceil(price) + 1
    else:
        price = ceil(price)
    # traffic jam price calculate
    jam_price = jam_time * 1.5
    if floor(jam_price) % 2 != 0:
        jam_price = floor(jam_price) - 1
    else:
        jam_price = floor(jam_price)
    print(int(price) + int(jam_price))

def price_check(distance):
    """ price per distance """
    if 0 <= distance <= 1:
        price = 35
    elif 2 <= distance <= 12:
        price = 5
    elif 13 <= distance <= 20:
        price = 5.50
    elif 21 <= distance <= 40:
        price = 6
    elif 41 <= distance <= 60:
        price = 6.50
    elif 61 <= distance <= 80:
        price = 7.50
    else:
        price = 8.50
    return price

main(int(input()), int(input()), 0)
