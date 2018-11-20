"""
GCD_N
Author : Chanwit Settavongsin
"""
def main(number):
    """
    Find highest common factor from N number
    """
    data = [int(input()) for _ in range(number)]
    frist = data[0]
    for i in range(1, len(data)):
        frist = gcd(frist, data[i])
    print(frist)

def gcd(num1, num2):
    """
    find highest common factor from 2 number
    Use Euclidean algorithm
    """
    return num1 if num2 == 0 else gcd(num2, num1 % num2)

main(int(input()))
