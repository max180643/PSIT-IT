"""
Divide3Or5
Author : Chanwit Settavongsin
"""
def main(number, answer):
    """ Find the sum of the numbers divisible by 3 and 5 """
    for i in range(1, number + 1):
        if i % 3 == 0 or i % 5 == 0:
            answer += i
    print(answer)

main(int(input()), 0)
