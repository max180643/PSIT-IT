"""Circular I"""
def main(pos1_x, pos1_y, radius, pos2_x, pos2_y):
    """Check Distant"""
    distant = ((pos1_x - pos2_x)**2 + (pos1_y - pos2_y)**2)**0.5
    if distant <= radius:
        print("Yes")
    else:
        print("No")

main(float(input()), float(input()), float(input()), float(input()), float(input()))
