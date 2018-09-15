"""
[EX] CookieClicker
Author : Chanwit Settavongsin
"""
def main(cost, produce, goal):
    """
    Get optimal way to play CookieClicker
    Input : cost -> farm price
            produce -> increase cookie rates
            goal -> required amount
    """
    time = 0 # initial time
    rate = 2 # production rate
    while True:
        if goal / rate < (goal / (rate + produce) + (cost / rate)):
            time += goal / rate
            break
        time += cost / rate # time to collect cookie to buy farm
        rate += produce # increase produce rate
    if time % 1 > 0:
        print("%.4f" % (time))
    else:
        print(int(time))

main(float(input()), float(input()), float(input()))
