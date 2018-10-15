"""
Missing Numbers
Author : Chanwit Settavongsin
"""
def main(number, temp):
    """ find missing number from 1 to number """
    check = []
    value = []
    for i in range(1, number + 1):
        check.append(i)
    while temp != 0:
        temp = int(input())
        value.append(temp)
    for i in value:
        if i in check:
            check.remove(i)
    for i in range(len(check)):
        print(check[i])

main(int(input()), 1)
