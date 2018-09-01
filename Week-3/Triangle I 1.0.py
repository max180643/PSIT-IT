"""
Triangle I
Author : Chanwit Settavongsin
"""
def main(num_1, num_2, num_3):
    """ Check can create triangle """
    # find top value
    num_1, num_2 = num_1 if num_1 < num_2 else num_2, num_1 if num_1 > num_2 else num_2
    num_1, num_3 = num_1 if num_1 < num_3 else num_3, num_1 if num_1 > num_3 else num_3
    num_2, num_3 = num_2 if num_2 < num_3 else num_3, num_2 if num_2 > num_3 else num_3
    # check
    temp = (num_1**2 + num_2**2)**0.5
    if num_3 - temp == 0 or num_3 - temp == 0.01:
        print("Yes")
    else:
        print("No")

main(float(input()), float(input()), float(input()))
