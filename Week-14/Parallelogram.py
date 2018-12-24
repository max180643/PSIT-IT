"""
Parallelogram
Author : Chanwit Settavongsin
"""
def main(text):
    """ Print Parallelogram text """
    for i in range(len(text) - 1, 0, -1):
        print("%s%s" % (" " * i, text[:len(text) - i]))
    for j in range(len(text)):
        print(text[j:])

main(input())
