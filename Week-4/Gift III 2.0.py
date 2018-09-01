"""
Gift III
Author : Chanwit Settavongsin
"""
def main(number, top, ans, temp):
    """ Find Number Before Top Number """
    for _ in range(number):
        num = int(input())
        if num > top:
            ans = top
            top = num
        elif num < top and num > ans:
            ans = num
        else:
            temp += 1
    print("Exit" if temp == number - 1 else ans)

main(int(input()), 0, 0, 0)
