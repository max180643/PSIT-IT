"""
Sequence XI
Author : Chanwit Settavongsin
"""
def main(number):
    """
    input number and print
    ex. input = 3
    print : 01 01 01 01 01
            01 02 02 02 01
            01 02 03 02 01
            01 02 02 02 01
            01 01 01 01 01
    """
    for i in range(1 - number, number):
        for j in range(1 - number, number):
            print("%02i " % (number - max(abs(i), abs(j))), end="")
        print()

main(int(input()))
