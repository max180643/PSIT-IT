"""
VerticalHistogram
Author : Chanwit Settavongsin
"""
def main(text, keyword, char, value):
    """ Print histogram of number's character """
    for key in keyword:
        if key in text:
            char.append(key)
            value.append(text.count(key))
    for i in range(max(value), 0, -1):
        print("%03d" % (i), end=" ")
        for j in value:
            print("*" if j >= i else " ", end=" ")
        print()
    print("   ", end=" ")
    for i in char:
        print(i, end=" ")

main(input(), "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", [], [])
