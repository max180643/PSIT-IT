"""
Triangle
Author : Chanwit Settavongsin
"""
def main(num):
    """
    input number and print
    ex. input = 5
    print :               05
                        04  04
                      03      03
                    02          02
                  01              01
    """
    for i in range(num, 0, -1):
        if i == num:
            print("%s%02d" % (" " * (i * 2 - 2), i))
        else:
            print("%s%02d%s%02d" % (" " * (i * 2 - 2), i, " " * ((num - i) * 4 - 2), i))

main(int(input()))
