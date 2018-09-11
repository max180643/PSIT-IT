"""
Sequence III
Author : Chanwit Settavongsin
"""
def main(number, temp):
    """ Print 1+round to n+round : n line """
    for _ in range(number):
        answer = ""
        temp += 1
        for j in range(1 + temp, number + temp + 1):
            answer += ("%i " % (j))
        print(answer)

main(int(input()), 0)
