"""
Kaprekar's Constant
Author : Chanwit Settavongsin
"""
def main(num, count):
    """ Count the number that use to create number to 6174 """
    while num != 6174:
        num1 = (num - (num % 1000)) // 1000
        num2 = ((num % 1000) - (num % 100)) // 100
        num3 = ((num % 100) - (num % 10)) // 10
        num4 = num % 10
        # s.ort m.ax to m.in
        for _ in range(3):
            if num2 > num1:
                num2, num1 = num1, num2
            if num3 > num2:
                num3, num2 = num2, num3
            if num4 > num3:
                num4, num3 = num3, num4
        value1 = int("%d%d%d%d" % (num1, num2, num3, num4)) # m.ax value
        value2 = int("%d%d%d%d" % (num4, num3, num2, num1)) # m.in value
        num = value1 - value2
        count += 1
    print(count)

main(int(input()), 0)
