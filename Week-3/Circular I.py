"""
Circular I
Author : Chanwit Settavongsin
"""
def main(pos1_x, pos1_y, radius, pos2_x, pos2_y):
    """
    Find the displacement between position 1 to position 2
    """
    distant = ((pos1_x - pos2_x)**2 + (pos1_y - pos2_y)**2)**0.5
    if distant <= radius:
        print("Yes")
    else:
        print("No")

main(float(input()), float(input()), float(input()), float(input()), float(input()))
