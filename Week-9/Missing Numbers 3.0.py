"""
Missing Numbers
Author : Chanwit Settavongsin
"""
def main(number, temp, answer):
    """ find missing number from 1 to number """
    _ = [answer.append(i) for i in range(1, number + 1)]
    while temp != 0:
        temp = int(input())
        if temp in answer:
            answer.remove(temp)
    _ = [print(i) for i in answer]

main(int(input()), 1, [])
