"""
Difference
Author : Chanwit Settavongsin
"""
def main(set_a, set_b, member_a, member_b):
    """ Print member of set_a - set_b """
    _ = [set_a.add(int(input())) for _ in range(member_a)]
    _ = [set_b.add(int(input())) for _ in range(member_b)]
    answer = [number for number in set_a - set_b]
    answer.sort()
    print(*answer)

main(set(), set(), int(input()), int(input()))
