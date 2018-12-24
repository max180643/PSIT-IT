"""
Inverter
Author : Chanwit Settavongsin
"""
def main(text, answer):
    """ Convert character 1 -> 0 , 0 -> 1"""
    for i in text:
        answer += "0" if i == "1" else "1"
    if int(answer) != 0:
        print(int(answer))

main(input(), "")
