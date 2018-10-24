"""
PickThemAgain
Author : Chanwit Settavongsin
"""
def main(text, answer):
    """ find number that number % 3 == 0 or number % 5 == 0 """
    text.reverse()
    for i in text:
        if int(i) % 3 == 0 or int(i) % 5 == 0:
            answer.append(i)
    if len(answer) == 0:
        print("Nope")
    else:
        _ = [print(i) for i in answer]

main(input().split(" "), [])
