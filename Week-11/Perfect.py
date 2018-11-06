"""
Perfect
Author : Chanwit Settavongsin
"""
def main(number, total):
    """ Count perfect number of number """
    for i in range(2, number + 1):
        if check(i):
            total = total + i
    print(total)

def check(number):
    """ Check perfect number """
    total = 1
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            total = total + (number / i) + i
    if total == number:
        return True
    return False

main(int(input()), 0)
