"""
[EX] PointInTriangle
Author : Chanwit Settavongsin
"""
def main():
    """
    if pos_x, pos_y in triangle print "in"
                not in triangle print "out"
                on one side of the triangle print "on"
    """
    # input
    x_1, y_1 = float(input()), float(input())
    x_2, y_2 = float(input()), float(input())
    x_3, y_3 = float(input()), float(input())
    pos_x, pos_y = float(input()), float(input())
    # overlap
    left = find_dist(x_1, y_1, x_2, y_2) == find_dist(x_1, y_1, pos_x, pos_y) + \
    find_dist(pos_x, pos_y, x_2, y_2)
    right = find_dist(x_1, y_1, x_3, y_3) == find_dist(x_1, y_1, pos_x, pos_y) + \
    find_dist(pos_x, pos_y, x_3, y_3)
    bottom = find_dist(x_2, y_2, x_3, y_3) == find_dist(x_2, y_2, pos_x, pos_y) + \
    find_dist(pos_x, pos_y, x_3, y_3)
    # check
    if left or right or bottom:
        print("on")
    elif 0.5 * abs((x_2 - x_3) * (y_1 - y_3) - (x_1 - x_3) * (y_2 - y_3)) == \
    0.5 * abs((x_2 - x_3) * (pos_y - y_3) - (pos_x - x_3) * (y_2 - y_3)) + \
    0.5 * abs((pos_x - x_3) * (y_1 - y_3) - (x_1 - x_3) * (pos_y - y_3)) + \
    0.5 * abs((x_2 - pos_x) * (y_1 - pos_y) - (x_1 - pos_x) * (y_2 - pos_y)):
        print("in")
    else:
        print("out")

def find_dist(pos_x1, pos_y1, pos_x2, pos_y2):
    """ Find the distance between the two points """
    return ((pos_x2 - pos_x1)**2 + (pos_y2 - pos_y1)**2)**0.5

main()
