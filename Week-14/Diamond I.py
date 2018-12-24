"""
Diamond I
Author : Chanwit Settavongsin
"""
def main(height, weight):
    """ Find max value column """
    for i in range(height):
        temp = input().split()
        if i == 0:
            answer = [int(i) for i in temp]
        else:
            temp = [int(i) for i in temp]
            for j in range(weight):
                answer[j] = answer[j] + temp[j]
    print(max(answer))

main(int(input()), int(input()))
