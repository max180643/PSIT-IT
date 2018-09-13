"""
Indicator_Right
Author : Chanwit Settavongsin
"""
def main(number, row):
    """
    input number and print
    ex. number = 7
        row = 5
    print : *******
             *******
              *******
             *******
            *******
    """
    half = row / 2
    top = int(half) + 1
    low = int(half)
    for i in range(top):
        print("%s%s" %(" " * i, "*" * number))
    for j in range(low-1, -1, -1):
        print("%s%s" %(" " * j, "*" * number))

main(int(input()), int(input()))
