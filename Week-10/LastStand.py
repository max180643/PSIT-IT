"""
LastStand
Author : Chanwit Settavongsin
"""
import json
def main(number):
    """ Print last digit of number in list """
    number = json.loads(number)
    _ = [print(i % 10) for i in number]

main(input())
