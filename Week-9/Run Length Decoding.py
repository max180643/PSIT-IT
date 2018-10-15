"""
Run Length Decoding
Author : Chanwit Settavongsin
"""
def main(text, total, char, number, answer):
    """ Decoding text """
    for i in text:
        if i.isalpha():
            char.append(i)
            total.append(number)
            number = ""
        elif i.isdigit():
            number += str(i)
    for j in range(len(char)):
        answer += "%s" % (char[j] * int(total[j]))
    print(answer)

main(input(), [], [], "", "")
