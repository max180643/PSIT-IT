"""
Sequence X
Author : Chanwit Settavongsin
"""
def main(number):
    """
    input number and print
    ex. input = 4
    print :
                01
             01 02 01
          01 02 03 02 01
       01 02 03 04 03 02 01
          01 02 03 02 01
             01 02 01
                01
    """
    # Upper
    for i in range(1, number + 1):
        print("%s" % ("   " * (number - i)), end="")
        for j in range(1, 2 * i):
            half = (2 * i - 1) // 2 + 1 # find center column
            if j <= half:
                print("%02i" % (j), end=" ")
            else:
                print("%02i" % (half - (j - half)), end=" ")
        print()
    # Lower
    for i in range(number - 1, 0, -1):
        print("%s" % ("   " * (number - i)), end="")
        for j in range(1, 2 * i):
            half = (2 * i - 1) // 2 + 1 # find center column
            if j <= half:
                print("%02i" % (j), end=" ")
            else:
                print("%02i" % (half - (j - half)), end=" ")
        print()

main(int(input()))
