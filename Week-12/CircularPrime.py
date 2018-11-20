"""
CircularPrime
Author : Chanwit Settavongsin
"""
def circular_prime_answer(number, total):
    """ Print sum of circular prime from 1 to number """
    for i in range(1, number + 1):
        if circular_prime(i):
            total += i
    print(total)

def circular_prime(number):
    """ Return true if number is circular prime else return false """
    for i in range(len(str(number))):
        # rotate number
        rotate = str(number)
        rotate = rotate[i:] + rotate[:i]
        rotate = int(rotate)
        # check prime number
        if not is_prime(rotate):
            return False
    return True

def is_prime(number):
    """ Return true if number is prime number else return false """
    if number == 1:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

circular_prime_answer(int(input()), 0)
