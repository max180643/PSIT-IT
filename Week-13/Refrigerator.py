"""
Refrigerator
Author : Chanwit Settavongsin
"""
def main(total, valid, answer):
    """ The maximum number of days that a food can be kept """
    valid.sort()
    while valid[0] != 0:
        for i in range(1, total):
            valid[i] = valid[i] - 1
        answer += 1
        valid.sort()
    print(answer)

main(int(input()), [int(valid) for valid in input().split()], 0)
