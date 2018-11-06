"""
FibonacciRecursionV1
Author : Chanwit Settavongsin
"""
def main(fib1, fib2, number, count):
    """ Find value of fibonnacci order n """
    fib1, fib2 = fib2, fib1 + fib2
    if number <= 1:
        print(number)
    elif count == number - 2:
        print(fib2)
    else:
        return main(fib1, fib2, number, count + 1)

main(0, 1, int(input()), 0)
