"""
HelloWorldComeBack
Author : Chanwit Settavongsin
"""
def main(text):
    """
    Check text if english language add 'Hello'
                  thai language add 'สวัสดี'
                  in front of text
    """
    for i in text:
        temp = i
        break
    if temp.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print("Hello %s." % (text))
    else:
        print("สวัสดี %s" % (text))

main(input())
