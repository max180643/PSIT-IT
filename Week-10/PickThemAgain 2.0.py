"""
PickThemAgain
Author : Chanwit Settavongsin
"""
def main(text, answer):
    """ find number that number % 3 == 0 or number % 5 == 0 """
    text.reverse()
    _ = [answer.append(i) for i in text if int(i) % 3 == 0 or int(i) % 5 == 0]
    if len(answer) == 0:
        print("Nope")
    else:
        print(*answer, sep="\n")

main(input().split(" "), [])
