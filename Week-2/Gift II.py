"""
Gift II
Author : Chanwit Settavongsin
"""
def main(ans):
    """ Find weight of gift is even """
    ans += check(int(input()))
    ans += check(int(input()))
    ans += check(int(input()))
    ans += check(int(input()))
    ans += check(int(input()))
    ans += check(int(input()))
    ans += check(int(input()))
    ans += check(int(input()))
    print(ans)

def check(weight):
    """ Check Weight is Even """
    ans = 0
    if weight % 2 == 0:
        ans = weight
    return ans

main(0)
