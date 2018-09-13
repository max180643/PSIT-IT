"""
Indicator_Right
Author : Chanwit Settavongsin
"""
def main(number, row):
    """
    input number and print
    ex. number = 7
        row = 5
                        i                         sol
    print : *******   |-2 : ' ' * (row // 2 - abs(i)) + '*' * number|
             *******  |-1 : ' ' * (row // 2 - abs(i)) + '*' * number|
              ******* | 0 : ' ' * (row // 2 - abs(i)) + '*' * number|
             *******  | 1 : ' ' * (row // 2 - abs(i)) + '*' * number|
            *******   | 1 : ' ' * (row // 2 - abs(i)) + '*' * number|
    """
    for i in range((1 - row) // 2, row // 2 + 1):
        print("%s%s" % (" " * (row // 2 - abs(i)), "*" * number))

main(int(input()), int(input()))
