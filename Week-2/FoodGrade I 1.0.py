"""FoodGrade I"""
def main(total):
    """Find Chicken"""
    print(call(total) + call(total))

def check(weight):
    """Check Rule"""
    return 1 if 50 <= weight <= 70 else 0

def call(total):
    """Call Function"""
    total += check(int(input()))+check(int(input()))+check(int(input()))+check(int(input()))+\
    check(int(input()))+check(int(input()))+check(int(input()))+check(int(input()))+\
    check(int(input()))+check(int(input()))+check(int(input()))+check(int(input()))
    return total

main(0)
