"""
Ink
Author : Chanwit Settavongsin
"""
def main(answer):
    """ Find flood time """
    area, number = input().split()
    for _ in range(int(number)):
        pos_x, pos_y = input().split()
        time = 3.1416 * (int(pos_x)**2 + int(pos_y)**2) / int(area)
        answer.append(int(time) if time == int(time) else int(time) + 1)
    print(*answer, sep="\n")

main([])
