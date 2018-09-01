"""
Timing
Author : Chanwit Settavongsin
"""
def main():
    """
    Convert input second to
    day, hour, minute, second and Print output
    """
    second = int(input())
    minute, second = divmod(second, 60)
    hour, minute = divmod(minute, 60)
    day, hour = divmod(hour, 24)
    print(day, hour, minute, second)

main()
