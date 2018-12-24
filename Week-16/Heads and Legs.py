"""
Heads and Legs
Author : Chanwit Settavongsin
"""
def main(head, leg):
    """ Find rabbit, bird"""
    rabbit = (leg - (2 * head)) / 2
    bird = head - rabbit
    if rabbit % 1 == 0 and bird % 1 == 0 and rabbit >= 0 and bird >= 0:
        print(int(rabbit), int(bird))
    else:
        print("Impossible")

main(int(input()), int(input()))
