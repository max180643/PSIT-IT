"""
dart
Author : Chanwit Settavongsin
"""
def main(arrow, temp, answer):
    """ Find dart score """
    for _ in range(arrow):
        temp = input().split()
        temp = distant(int(temp[0]), int(temp[1]))
        if temp >= 0 and temp <= 2:
            answer += 5
        elif temp > 2 and temp <= 4:
            answer += 4
        elif temp > 4 and temp <= 6:
            answer += 3
        elif temp > 6 and temp <= 8:
            answer += 2
        elif temp > 8 and temp <= 10:
            answer += 1
    print(answer)

def distant(var_x, var_y):
    """ find distant between 2 point """
    return ((var_x**2) + (var_y**2))**0.5

main(int(input()), "", 0)
