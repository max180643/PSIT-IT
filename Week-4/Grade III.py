"""
Grade III
Author : Chanwit Settavongsin
"""
def check(score):
    """ Check Score Return Grade """
    temp = 0
    if 100 >= score >= 95:
        temp = 4
    elif 95 > score >= 90:
        temp = 3.5
    elif 90 > score >= 85:
        temp = 3
    elif 85 > score >= 80:
        temp = 2.5
    elif 80 > score >= 75:
        temp = 2
    elif 75 > score >= 70:
        temp = 1.5
    elif 70 > score >= 65:
        temp = 1
    elif 65 > score >= 60:
        temp = 0.5
    return temp

def main(subject, ans):
    """ Find Average Grade """
    for _ in range(subject):
        ans += check(float(input()))
    print("%.2f" % ((ans*100//subject)/100))

main(int(input()), 0)
