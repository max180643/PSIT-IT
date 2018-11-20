"""
PedPonFire
Author : Chanwit Settavongsin
"""
import math as m
def main(total, duck):
    """ Find the number of ducks that fly the maximum """
    for _ in range(total):
        duck.append(int(input()))
    abstract = int(input())
    duck.sort()
    set_duck = sorted(set(duck))
    check = duck.count(abstract / 2)
    answer = 0 if check <= 1 else m.factorial(check)//(m.factorial(check - 2) * m.factorial(2))
    for i in set_duck:
        if i >= abstract / 2:
            break
        answer += duck.count(abstract - i) * duck.count(i)
    print(answer)

main(int(input()), [])
