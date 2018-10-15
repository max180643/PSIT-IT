"""
CoPrimeV1
Author : Chanwit Settavongsin
"""
def main(number1, number2, answer):
    """ if highest common factor is 1 print yes else print 0 """
    min_value, max_value = min(number1, number2), max(number1, number2)
    value = max_value if min_value == 0 else min_value
    for i in range(value, 0, -1):
        if number1 % i == 0 and number2 % i == 0:
            answer = i
            break
    else:
        answer = value
    if answer == 1:
        print("YES", answer, sep="\n")
    else:
        print("NO", answer, sep="\n")

main(int(input()), int(input()), 0)
