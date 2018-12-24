"""
Point Sorting
Author : Chanwit Settavongsin
"""
def main(number, answer):
    """ Sorting """
    for _ in range(number):
        box = []
        number_set = int(input())
        for _ in range(number_set):
            temp = input().split()
            box.append([int(temp[0]), int(temp[1])])
        box.sort(key=lambda x: (x[0] + x[1], x[0]))
        answer.append(box)
    for i in range(number):
        for j in range(len(answer[i])):
            print(answer[i][j][0], answer[i][j][1], sep=" ")

main(int(input()), [])
