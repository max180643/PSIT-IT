"""
Nearer
Author : Chanwit Settavongsin
"""
def main(alice, bob, shop):
    """ Find the nearest people """
    if abs(shop - alice) < abs(shop - bob):
        print("Alice %d" % (abs(shop - alice)))
    elif abs(shop - bob) < abs(shop - alice):
        print("Bob %d" % (abs(shop - bob)))
    else:
        print("Sundaes %d" % (abs(shop - alice)))

main(int(input()), int(input()), int(input()))
