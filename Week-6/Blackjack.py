"""
Blackjack
Author : Chanwit Settavongsin
"""
def main(card, temp, score):
    """ find best score of card in you hand """
    for _ in range(card):
        point_card = input()
        if point_card == "A":
            temp += 1
        elif point_card == "J" or point_card == "K" or point_card == "Q":
            score += 10
        else:
            score += int(point_card)
    if temp != 0:
        for _ in range(temp):
            if score + 11 * temp <= 21:
                score += 11
                temp -= 1
            else:
                score += 1
                temp -= 1
    print(score)

main(int(input()), 0, 0)
