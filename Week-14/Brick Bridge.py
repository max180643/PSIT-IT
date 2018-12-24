"""
Brick Bridge
Author : Chanwit Settavongsin
"""
def main(brick_small, brick_big, goal):
    """ Find small brick used """
    check = goal // 5
    if check > brick_big:
        goal -= brick_big * 5
    else:
        goal -= check * 5
    if brick_small - goal >= 0:
        answer, goal = goal, 0
        print(answer)
    else:
        print("-1")

main(int(input()), int(input()), int(input()))
