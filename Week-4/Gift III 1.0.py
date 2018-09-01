"""
Gift III
Author : Chanwit Settavongsin
"""
def main(number):
    """ Find Number Before Top Number """
    top = 0
    ans = 0
    temp = 0
    for _ in range(number):
        num = int(input())
        if num > top:
            ans = top
            top = num
        elif num < top and num > ans:
            ans = num
        else:
            temp += 1

    if temp == number - 1:
        print("Exit")
    else:
        print(ans)

main(int(input()))
