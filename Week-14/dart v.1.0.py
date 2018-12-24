"""
dart
Author : Chanwit Settavongsin
"""
import math
def main(arrow, temp, answer):
    """ Find dart score """
    for _ in range(arrow):
        temp = input().split()
        temp = (math.pi * (distant(int(temp[0]), int(temp[1]))))**2
        if temp <= (math.pi * 2) ** 2:
            answer += 5
        elif temp <= (math.pi * 4) ** 2:
            answer += 4
        elif temp <= (math.pi * 6) ** 2:
            answer += 3
        elif temp <= (math.pi * 8) ** 2:
            answer += 2
        elif temp <= (math.pi * 10) ** 2:
            answer += 1
    print(answer)

def distant(var_x, var_y):
    """ find distant between 2 point """
    return (((var_x - 0)**2) + ((var_y - 0)**2))**0.5

main(int(input()), "", 0)
