"""
Frame
Author : Chanwit Settavongsin
"""
def main(text):
    """ print text in frame """
    print("%s" % ("*" * (len(text) + 2)))
    print("*%s*" % (text))
    print("%s" % ("*" * (len(text) + 2)))

main(input())
