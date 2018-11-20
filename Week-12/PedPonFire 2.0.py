"""
PedPonFire
Author : Chanwit Settavongsin
"""
def main(duck, abstract, answer):
    """ Find the number of ducks that fly the maximum """
    set_duck = sorted(set(duck))
    for i in set_duck:
        if i > abstract / 2:
            break
        answer += duck.count(abstract - i) * duck.count(i)
    print(answer)

main(sorted([int(input()) for _ in range(int(input()))]), int(input()), 0)
