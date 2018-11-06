"""
SqFree
Author : Chanwit Settavongsin
"""
def main(number, answer):
    """ Count square-free number in 1 to n """
    for i in range(1, number+1):
        for j in range(2, int(i**0.5)+1):
            if i % (j**2) == 0:
                answer += 1
                break
    print(number - answer)

main(int(input()), 0)
