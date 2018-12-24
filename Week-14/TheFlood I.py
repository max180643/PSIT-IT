"""
TheFlood I
Author : Chanwit Settavongsin
"""
def main(status, answer):
    """ Most time to resist flood """
    while 0 not in status:
        status.sort()
        for i in range(1, len(status)):
            status[i] -= 1
        answer += 1
    print(answer)

main([int(i) for i in input().split()], 0)
