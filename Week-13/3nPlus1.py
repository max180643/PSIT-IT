"""
3nPlus1
Author : Chanwit Settavongsin
"""
def main(answer):
    """ input value and value != 0 """
    while True:
        number = int(input())
        if number == 0:
            break
        else:
            answer.append(check(number, 1))
    print(*answer, sep="\n")

def check(number, total):
    """ Check number """
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        total += 1
    return total

main([])
