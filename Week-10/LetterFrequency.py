"""
LetterFrequency
Author : Chanwit Settavongsin
"""
def main(text, char, total):
    """ find the most character in list """
    _ = [char.append(i) for i in text if i.isalpha() and i not in char]
    _ = [total.append(text.count(i)) for i in char]
    index = total.index(max(total))
    print(char[index])

main(input().lower(), [], [])
