"""
Day I
Author : Chanwit Settavongsin
"""
def main(year):
    """
    Check leaf year
    If year divisible by 4 but not divisible by 100
    or year divisible by 400 is a leap year
    """
    print("Yes" if (year % 4) == 0 and ((year % 100) != 0 or (year % 400) == 0) else "No")

main(int(input()))
