"""
isprime_small
Author : Chanwit Settavongsin
"""
def main():
    """ Check is prime number """
    number = int(input())
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                print("No")
                break
        else:
            print("Yes")
    else:
        print("No")

main()
