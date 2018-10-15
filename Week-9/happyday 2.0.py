"""
happyday
Author : Chanwit Settavongsin
"""
def main(answer):
    """ Count happyday in list """
    happy = input().split(",")
    for i in range(len(happy)):
        if int(happy[i]) >= 80:
            answer += 1
        elif i != 0:
            if int(happy[i]) >= 20 and int(happy[i]) - int(happy[i-1]) >= 10:
                answer += 1
    print(answer)

main(0)
