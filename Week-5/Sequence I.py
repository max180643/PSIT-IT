"""
Sequence I
Author : Chanwit Settavongsin
"""
def main(number):
    """ Print 1 to n : n line """
    for _ in range(number):
        answer = ""
        for i in range(1, number + 1):
            answer += ("%i " % (i))
        print(answer)

main(int(input()))
