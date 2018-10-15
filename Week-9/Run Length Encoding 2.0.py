"""
Run Length Encoding
Author : Chanwit Settavongsin
"""
def main(text, answer, word, final):
    """ Encoding text """
    temp = text[0]
    for char in text:
        if temp != char:
            answer.append(word)
            temp, word = char, char
        else:
            word += char
    for group in answer:
        final += "%s%s" % (len(group), group[0])
    print(final)

main(input() + "#", [], "", "")
