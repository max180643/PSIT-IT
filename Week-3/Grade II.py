"""
Grade II
Author : Chanwit Settavongsin
"""
def main(score):
    """ Check score and Print grade """
    if 100 >= score >= 95:
        print("A")
    elif 95 > score >= 90:
        print("B+")
    elif 90 > score >= 85:
        print("B")
    elif 85 > score >= 80:
        print("C+")
    elif 80 > score >= 75:
        print("C")
    elif 75 > score >= 70:
        print("D+")
    elif 70 > score >= 65:
        print("D")
    elif 65 > score >= 60:
        print("F+")
    elif 60 > score >= 0:
        print("F")
    else:
        print("ERR")

main(float(input()))
