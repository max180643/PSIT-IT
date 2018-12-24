"""
BookWorm
Author : Chanwit Settavongsin
"""
def main(number):
    """ Print number of book can we read """
    for _ in range(number):
        time, check, answer = int(input()), 0, 0
        book = sorted([int(input()) for _ in range(int(input()))])
        for i in book:
            check += i
            if check > time:
                break
            answer += 1
        print(answer)

main(int(input()))
