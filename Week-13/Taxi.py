"""
Taxi
Author : Chanwit Settavongsin
"""
from math import floor, ceil
def main(distance, jam_time, price):
    """ Calculate Taxi Price """
    while True:
        text = input().split()
        if text[0] == 'F':
            break
        elif text[0] == 'K':
            distance += int(text[1])
        elif text[0] == 'W':
            if text[2] != '0':
                distance += int(text[2])
            jam_time += int(text[1])
    # calculate money
    if distance == 0:
        print(35)
    else:
        for i in range(1, distance + 1):
            price += price_check(i)
        print((ceil(price) + 1 if ceil(price)%2 == 0 else ceil(price)) + \
             (floor(jam_time*1.5) - 1 if floor(jam_time*1.5)%2 != 0 else floor(jam_time*1.5)))

def price_check(distance):
    """ price check """
    if distance == 1:
        price = 35
    elif 2 <= distance <= 12:
        price = 5
    elif 13 <= distance <= 20:
        price = 5.5
    elif 21 <= distance <= 40:
        price = 6
    elif 41 <= distance <= 60:
        price = 6.5
    elif 61 <= distance <= 80:
        price = 7.5
    else:
        price = 8.5
    return price

main(0, 0, 0)
