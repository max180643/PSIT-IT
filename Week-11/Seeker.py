"""
Seeker
Author : Chanwit Settavongsin
"""
def main(text, data, answer, temp, number):
    """ Extract number from text and sum all number """
    for char in text:
        if char.isdecimal():
            number += char
        elif temp.isdecimal():
            data.append(int(number))
            number = ""
        temp = char
    for i in data:
        answer += i
    print(answer)

main(input() + "#", [], 0, "", "")
