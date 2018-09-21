"""
Align
Author : Chanwit Settavongsin
"""
from math import ceil, floor
def main(length, align, text):
    """ Print text and set format"""
    if align == "left":
        print(text)
    elif align == "right":
        print("%s%s" % (" " * (length - len(text)), text))
    else:
        half = (length - len(text)) / 2
        print("%s%s%s" % (" " * ceil(half), text, " " * floor(half)))

main(int(input()), input(), input())
