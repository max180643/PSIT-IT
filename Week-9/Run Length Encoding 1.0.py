"""
Run Length Encoding
Author : Chanwit Settavongsin
"""
def main(text, total, char, answer):
    """ Encoding text """
    temp, number = "temp", 0
    for i in text:
        if i == temp:
            number += 1
        elif i != temp and number == 0:
            char.append(i)
            number += 1
            temp = i
        elif i != temp and number > 0:
            total.append(number)
            number = 0
            char.append(i)
            number += 1
            temp = i
    total.append(number)
    for j in range(len(char)):
        answer += "%s" % (str(total[j]) + char[j])
    print(answer)

main(input(), [], [], "")
