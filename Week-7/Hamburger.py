"""
Hamburger
Author : Chanwit Settavongsin
"""
def main(left, right):
    """
    input number and print
    ex. input = 2
                3
    print :
           ||**********|||
    """
    print("%s%s%s" % ("|" * left, "*" * ((left + right) * 2), "|" * right))

main(int(input()), int(input()))
