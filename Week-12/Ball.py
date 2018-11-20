"""
Ball
Author : Chanwit Settavongsin
"""
def main(height, answer):
    """ Find number that ball bounce """
    while height >= 0.01:
        height, answer = height * (3/5), answer + 1
    print(answer)

main(float(input()), -1)
