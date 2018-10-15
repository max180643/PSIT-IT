"""
happyday
Author : Chanwit Settavongsin
"""
def main(check, before, answer):
    """ Count happyday in list """
    happy = input().split(",")
    for number in happy:
        if int(number) >= 80 and check == 1:
            answer += 1
        elif int(number) >= 80 or (int(number) >= 20 and int(number) >= before + 10) and check == 0:
            answer += 1
        before = int(number)
        check = 0
    print(answer)

main(1, 0, 0)
