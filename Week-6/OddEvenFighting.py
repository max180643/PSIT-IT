"""
OddEvenFighting
Author : Chanwit Settavongsin
"""
def main(even, odd):
    """
    find total of even number and odd number
    and check:
              even > odd : print "Even", even's total
              odd > even : print "Odd", odd's total
              draw : print "Draw", total
    """
    while True:
        number = int(input())
        if number == 0:
            break
        elif number % 2 == 0:
            even += number
        else:
            odd += number
    if even == odd:
        print("Draw %i" % (even))
    elif even > odd:
        print("Even %i" % (even))
    else:
        print("Odd %i" % (odd))

main(0, 0)
