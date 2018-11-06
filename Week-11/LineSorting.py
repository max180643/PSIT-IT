"""
LineSorting
Author : Chanwit Settavongsin
"""
def main(number, text):
    """ Sort string from length and Print """
    _ = [text.append(input()) for _ in range(number)]
    text.sort(key=len)
    print(*text, sep="\n")

main(int(input()), [])
