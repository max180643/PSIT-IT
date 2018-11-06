"""
GCD_v2
Author : Chanwit Settavongsin
"""
def main(num1, num2):
    """
    find highest common factor from 2 number
    Use Euclidean algorithm
    """
    if num2 == 0:
        print(num1)
    else:
        main(num2, num1 % num2)

main(int(input()), int(input()))
