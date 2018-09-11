"""
Sequence VIII
Author : Chanwit Settavongsin
"""
def main(number, temp):
    """
    input number and print
    ex. input = 3
    print :       01
               01 02
            01 02 03
    """
    for i in range(1, number + 1):
        print("%s" % ("   " * (number - i)), end="")
        for j in range(1, temp + 1):
            print("%02d" % (j), end=" ")
        print()
        temp += 1

main(int(input()), 1)
