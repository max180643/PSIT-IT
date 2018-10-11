"""
Largest Number
Author : Chanwit Settavongsin
"""
def main(num1, num2, num3, ans):
    """ S.ort 3 group of number to create largest number """
    if num1 != 0 or num2 != 0 or num3 != 0:
        case1 = int(str(num2) + str(num1) + str(num3))
        case2 = int(str(num3) + str(num1) + str(num2))
        case3 = int(str(num1) + str(num2) + str(num3))
        case4 = int(str(num3) + str(num2) + str(num1))
        case5 = int(str(num1) + str(num3) + str(num2))
        case6 = int(str(num2) + str(num3) + str(num1))
        ans = case1 if case1 > ans else ans
        ans = case2 if case2 > ans else ans
        ans = case3 if case3 > ans else ans
        ans = case4 if case4 > ans else ans
        ans = case5 if case5 > ans else ans
        ans = case6 if case6 > ans else ans
    print(ans)

main(int(input()), int(input()), int(input()), 0)
