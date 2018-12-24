"""
Quardrant
Author : Chanwit Settavongsin
"""
def main(var_x, var_y):
    """ Find quardrant of var_x, var_y """
    if var_x == 0 and var_y == 0:
        print("O")
    elif var_y == 0:
        print("X")
    elif var_x == 0:
        print("Y")
    elif var_x > 0 and var_y > 0:
        print("Q1")
    elif var_x < 0 and var_y > 0:
        print("Q2")
    elif var_x < 0 and var_y < 0:
        print("Q3")
    elif var_x > 0 and var_y < 0:
        print("Q4")

main(int(input()), int(input()))
