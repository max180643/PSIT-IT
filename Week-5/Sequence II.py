"""
Sequence II
Author : Chanwit Settavongsin
"""
def main(number, answer):
    """ print i**2 in range(1, n) """
    for i in range(1, number + 1):
        answer += ("%i " % (i**2))
    print(answer)

main(int(input()), "")
