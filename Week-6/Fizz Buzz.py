"""
Fizz Buzz
Author : Chanwit Settavongsin
"""
def main(number):
    """
    print 1 to n
    number % 3 == 0 print "Fizz"
    number % 5 == 0 print "Buzz"
    number % 3 and 5 == 0 print "Fizz Buzz"
    """
    for i in range(1, number + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz Buzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

main(int(input()))
