"""
Sequence IV
Author : Chanwit Settavongsin
"""
def main(number):
    """
    input number and print
    ex. input = 5
    print : 1 2 3 4 5 = 5x0 + 1 2 3 4 5
            6 7 8 9 10 = 5x1 + 1 2 3 4 5
            11 12 13 14 15 = 5x2 + 1 2 3 4 5
            16 17 18 19 20 = 5x3 + 1 2 3 4 5
            21 22 23 24 25 = 5x4 + 1 2 3 4 5
    """
    for i in range(number):
        answer = ""
        for j in range(1, number + 1):
            answer += ("%i " % (i * number + j))
        print(answer)

main(int(input()))
