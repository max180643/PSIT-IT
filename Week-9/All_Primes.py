"""
All_Primes
Author : Chanwit Settavongsin
"""
def main(number):
    """ How much prime number from 1 to n """
    total = 0
    for i in range(1, number + 1):
        total += check(i)
    print(total)

def check(number):
    """ Check prime number """
    answer = 0
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            answer = 1
    return answer

main(int(input()))
