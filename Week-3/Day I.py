"""Day I"""
def main(year):
    """Check leafyear"""
    print("Yes" if (year % 4) == 0 and ((year % 100) != 0 or (year % 400) == 0) else "No")

main(int(input()))
