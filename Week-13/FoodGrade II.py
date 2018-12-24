"""
FoodGrade II
Author : Chanwit Settavongsin
"""
def main(size, item, answer):
    """ find max number to collect item in box """
    item = list(map(int, item))
    item.sort()
    for number in item:
        if size - number >= 0:
            size -= number
            answer += 1
    print(answer)

main(int(input()), input().split(), 0)
