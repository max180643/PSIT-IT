"""
Sequence VII
Author : Chanwit Settavongsin
"""
def main(number, temp, check):
    """
    input number and print
    ex. input = 3
    print : 1
            1 2
            1 2 3
            1 2
            1
    """
    for _ in range(number * 2 - 1):
        answer = ""
        if temp == number:
            check = -1
        for i in range(1, temp + 1):
            answer += ("%i " % (i))
        temp += check
        print(answer)

main(int(input()), 1, 1)
