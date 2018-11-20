"""
Gram_v1
Author : Chanwit Settavongsin
"""
def main(text, count):
    """ Find the most 2-gram """
    word_list = [text[i:i+2] for i in range(len(text) - 1)]
    for word in word_list:
        if word_list.count(word) > count:
            answer = word
            count = word_list.count(word)
    print(answer, count, sep="\n")

main(input(), 0)
