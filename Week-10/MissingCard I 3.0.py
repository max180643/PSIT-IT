"""
MissingCard I
Author : Chanwit Settavongsin
"""
def main(key, card):
    """ Find missing card """
    _ = [card.append(rank + suit) for rank in key for suit in "SHDC"]
    _ = [card.remove(input()) for i in range(51)]
    print(card[0])

main(["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"], [])
