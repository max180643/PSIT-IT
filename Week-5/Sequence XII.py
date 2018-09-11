"""
Sequence XII
Author : Chanwit Settavongsin
"""
def main(number):
    """
    input number and print
    ex. input = 3
    print : 03 02 01 02 03
            02 03 02 03 02
            01 02 03 02 01
            02 03 02 03 02
            03 02 01 02 03
    """
    for i in range(1 - number, number):
        for j in range(1 - number, number):
            print("%02i " % (number - abs(abs(i) - abs(j))), end="")
        print()

main(int(input()))
