"""Additive"""
from math import sin, cos, radians, factorial, sqrt, log
def main():
    """Print Equation"""
    print((sin(radians(90)) + sin(radians(60))**2) / (cos(radians(245**2)) + cos(radians(45+135))))
    print((factorial(16)*factorial(4)) / factorial(8))
    print((15+25) / sqrt((25-12)**2+(12-15)**2))
    print(log(1234**4, 10))
    print((log(4234, 5)+log(8191, 2)+71*log(156154, 10)) / (log(777, 7)-log(888, 8)-log(999, 9)))

main()
