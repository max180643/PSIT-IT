"""
Train
Author : Chanwit Settavongsin
"""
def main(text1, text2, total):
    """
    Print Text
    line1 : print (input string1 + input string2)
    line2 : print (input string1 + input string2) * total
    """
    print(text1+text2, ((text1+text2)*total), sep="\n")

main(input(), input(), int(input()))
