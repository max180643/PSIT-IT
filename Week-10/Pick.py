"""
Pick
Author : Chanwit Settavongsin
"""
import json
def main(text, keyword):
    """ if keyword in dict show value of key """
    text = json.loads(text)
    print("%s\n%s" % ("Yes", text.get(keyword)) if keyword in text.keys() else "No")

main(input(), input())
