"""
Table I
Author : Chanwit Settavongsin
"""
def main(number):
    """
    Print 15 x n (multiple table)
    Ex. n = 10
    output : 15 x 1 = 15
             15 x 2 = 30
             .
             .
             15 x 10 = 150
    """
    for i in range(1, number + 1):
        print("15 x %i = %i" % (i, 15 * i))

main(int(input()))
