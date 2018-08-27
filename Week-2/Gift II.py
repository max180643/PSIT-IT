"""Gift II"""
def main(ans):
    """Find Gift"""
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
    """Check Weight is Even"""
    ans = 0
    if weight % 2 == 0:
        ans = weight
    return ans

main(0)
