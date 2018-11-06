"""
FibonacciRecursionV2
Author : Chanwit Settavongsin
"""
def main(number):
    """ Find value of fibonnacci order n """
    print(fib(number)[0])

def fib(number):
    """
    Fibonanci
    ref : https://en.wikipedia.org/wiki/Exponentiation_by_squaring
          https://www.nayuki.io/page/fast-fibonacci-algorithms
    """
    if number == 0:
        return 0, 1
    else:
        var_a, var_b = fib(number//2)
        var_c = var_a*(var_b * 2 - var_a)
        var_d = var_a * var_a + var_b * var_b
        if number % 2 == 0:
            return var_c, var_d
        else:
            return var_d, var_c + var_d

main(int(input()))
