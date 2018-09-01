"""
FoodGrade I
Author : Chanwit Settavongsin
"""
def main(weight, total, count):
    """
    Find number of chicken weight between 50 - 70
    """
    if count < 24:
        main(int(input()), total + (1 if 50 <= weight <= 70 else 0), count + 1)
    else:
        print(total + (1 if 50 <= weight <= 70 else 0))

main(int(input()), 0, 1)
