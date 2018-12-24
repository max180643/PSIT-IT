"""
Kabata
Author : Chanwit Settavongsin
"""
def main(number, answer):
    """ Kabata language check """
    for _ in range(number):
        text = input()
        if text.find("baka") != -1:
            answer.append("no")
            continue
        text = text.replace("bakka", "").replace("ta", "").replace("ba", "").replace("ka", "")
        if len(text) == 0:
            answer.append("yes")
        else:
            answer.append("no")
    print(*answer, sep="\n")

main(int(input()), [])
