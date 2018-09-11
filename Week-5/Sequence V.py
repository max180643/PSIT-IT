"""
Sequence V
Author : Chanwit Settavongsin
"""
def main(number, total, answer):
    """
    input number and print
    ex. input = 8
    print : 8 7 6 5 4 3 2
            1
    """
    for i in range(number, 0, -1):
        if total == 7:
            answer += ("%i\n" % (i))
            total = 1
        else:
            answer += ("%i " % (i))
            total += 1
    print(answer)

main(int(input()), 1, "")
