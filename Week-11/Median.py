"""
Median
Author : Chanwit Settavongsin
"""
def main(number, data):
    """ Find median in list """
    _ = [data.append((int(input()))) for _ in range(number)]
    data.sort()
    if len(data) % 2 == 1:
        print("%.1f" % (data[number//2]))
    else:
        print("%.1f" % ((data[number//2-1] + data[number//2])/2))

main(int(input()), [])
