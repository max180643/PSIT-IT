"""
FoodGrade I
Author : Chanwit Settavongsin
"""
def main(total):
    """ Find number of chicken weight between 50 - 70 """
    print(call(total) + call(total))

def check(weight):
    """ Check chicken weight """
    return 1 if 50 <= weight <= 70 else 0

def call(total):
    """ Call Function """
    total += check(int(input()))+check(int(input()))+check(int(input()))+check(int(input()))+\
    check(int(input()))+check(int(input()))+check(int(input()))+check(int(input()))+\
    check(int(input()))+check(int(input()))+check(int(input()))+check(int(input()))
    return total

main(0)
