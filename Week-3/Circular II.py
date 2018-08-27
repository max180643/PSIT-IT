"""Circular II"""
def main():
    """Check Overlapping Area"""
    # input
    pos1_x, pos1_y, radius1 = float(input()), float(input()), float(input())
    pos2_x, pos2_y, radius2 = float(input()), float(input()), float(input())
    # check
    distant = ((pos1_x - pos2_x)**2 + (pos1_y - pos2_y)**2)**0.5
    if radius1 + radius2 > distant:
        print("Yes")
    else:
        print("No")

main()
