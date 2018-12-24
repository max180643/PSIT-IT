"""
WordSequence I
Author : Chanwit Settavongsin
"""
def main(text):
    """ Print text """
    for i in range(1, len(text) + 1):
        print(text[:i])

main(input())
