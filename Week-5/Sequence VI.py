"""
Sequence VI
Author : Chanwit Settavongsin
"""
def main(number, temp):
    """
    input number and print
    ex. input = 5
    print : 1
            1 2
            1 2 3
            1 2 3 4
            1 2 3 4 5
    """
    for _ in range(number):
        answer = ""
        temp += 1
        for i in range(1, temp + 1):
            answer += ("%i " % (i))
        print(answer)

main(int(input()), 0)
