"""
RemoveTag
Author : Chanwit Settavongsin
"""
def main(text, status, word, answer):
    """ Remove html tag from string and store in list """
    for i in text:
        if i == "<":
            status = "unstored"
        elif i == ">":
            status = "stored"
        if status == "stored" and i != ">":
            word += i
        elif status == "unstored" and i == "<":
            answer.extend(word.split())
            word = ""
    print(answer)

main(input() + "<", "stored", "", [])
