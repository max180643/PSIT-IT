"""
SqFree
Author : Chanwit Settavongsin
"""
def main(number, temp, answer):
    """ Count square-free number in 1 to n """
    for i in range(1, number+1):
        for j in range(2, int(i**0.5)+1):
            if i % (j**2) == 0:
                temp += 1
        if temp > 0:
            answer += 1
        temp = 0
    print(number - answer)

main(int(input()), 0, 0)
