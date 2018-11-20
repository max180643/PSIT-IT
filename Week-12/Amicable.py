"""
Amicable
Author : Chanwit Settavongsin
"""
def main(range_total, amicable):
    """ Find the sum of amicable numbers """
    for i in range(2, range_total + 1):
        if i not in amicable:
            number = proper_divisor(i)
            if proper_divisor(number) == i and i != number:
                amicable.append(i)
                amicable.append(number)
    print(sum(amicable))

def proper_divisor(number):
    """ Find sum of proper """
    proper = 1
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            proper += i + number // i
    return proper

main(int(input()), [])
