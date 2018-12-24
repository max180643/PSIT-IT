"""
OneTwo
Author : Chanwit Settavongsin
"""
def main(number, temp):
    """
    S1 = "1"
    S2 = "2"
    Sn = Sn-1 + Sn-2
    print Sn
    """
    for i in range(3, number + 1):
        if not i in temp:
            temp[i] = temp[i - 1] + temp[i - 2]
    print(temp[number])

main(int(input()), {1:'1', 2:'2'})
