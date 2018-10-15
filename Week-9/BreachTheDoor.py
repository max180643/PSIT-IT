"""
BreachTheDoor
Author : Chanwit Settavongsin
"""
def main(text, answer):
    """
    find text that length more than 6
    and remove special characters, number
    """
    keyword = "abcdefghijklmnopqrstuvwxyz"
    text = text.split(" ")
    for word in text:
        temp = ""
        for i in range(len(word)):
            if word[i].lower() in keyword:
                temp += word[i]
        if len(temp) > 6:
            answer.append(temp)
    _ = [print(ans, end=" ") for ans in answer]

main(input(), [])
