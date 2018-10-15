"""
AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain
Author : Chanwit Settavongsin
"""
def main(text, answer):
    """ Print word that have 2 vowel """
    vowel = ["a", "e", "i", "o", "u"]
    text = (text.replace(".", "")).split(" ")
    for word in text:
        temp = 0
        for i in vowel:
            temp += (word.lower()).count(i)
        if temp >= 2:
            answer.append(word)
    answer.sort()
    if len(answer) > 0:
        for ans in answer:
            print(ans)
    else:
        print("Nope")

main(input(), [])
