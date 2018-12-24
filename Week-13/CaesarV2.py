"""
CaesarV2
Author : Chanwit Settavongsin
"""
def main(text, answer):
    """ Caesar Cipher decode """
    for key in range(1, 27):
        for i in text:
            if i.isalpha():
                check = 65 if i.isupper() else 97
                i = chr((ord(i) - check + key) % 26 + check)
            answer += i
        if "the" in answer.lower().split():
            print(answer)
            break
        answer = ""

main(input(), "")
