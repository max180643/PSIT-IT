"""
Regulation
Author : Chanwit Settavongsin
"""
def main(num1, num2, str1):
    """ Print Output """
    print("%30i" % (num1))
    print("%030i" % (num1))
    print("%.2f" % (num2))
    print("%.12f" % (num2))
    print("%40s" % (str1))

main(int(input()), float(input()), input())
