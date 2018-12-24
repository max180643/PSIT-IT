"""
WordSequence II
Author : Chanwit Settavongsin
"""
def main(text1, text2):
    """ Print text """
    print(text1)
    for i in range(1, max(len(text1), len(text2)) + 1):
        print(text2[:i] + text1[i:])

main(input(), input())
