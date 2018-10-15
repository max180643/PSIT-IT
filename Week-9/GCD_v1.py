"""
GCD_v1
Author : Chanwit Settavongsin
"""
def main(number1, number2):
    """ find highest common factor from 2 number """
    min_value, max_value = min(number1, number2), max(number1, number2)
    value = max_value if min_value == 0 else min_value
    for i in range(value, 0, -1):
        if number1 % i == 0 and number2 % i == 0:
            print(i)
            break
    else:
        print(value)

main(int(input()), int(input()))
