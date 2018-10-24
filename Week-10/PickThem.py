"""
PickThem
Author : Chanwit Settavongsin
"""
import json
def main(number, answer):
    """ find even number in list """
    number = json.loads(number)
    _ = [answer.append(i) for i in number if i % 2 == 0]
    if len(answer) > 0:
        print(*answer, sep="\n")
    else:
        print("Nope")

main(input(), [])
