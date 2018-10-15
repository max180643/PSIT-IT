"""
Ascending
Author : Chanwit Settavongsin
"""
def main(number):
    """ Sort Number & Print """
    for _ in range(5):
        number.append(int(input()))
    number.sort()
    for i in range(5):
        print(number[i])

main([])
