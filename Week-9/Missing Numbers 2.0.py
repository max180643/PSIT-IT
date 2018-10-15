"""
Missing Numbers
Author : Chanwit Settavongsin
"""
def main(number, temp, answer):
    """ find missing number from 1 to number """
    for i in range(1, number + 1):
        answer.append(i)
    while temp != 0:
        temp = int(input())
        if temp in answer:
            answer.remove(temp)
    for i in range(len(answer)):
        print(answer[i])

main(int(input()), 1, [])
