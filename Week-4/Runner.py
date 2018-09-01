"""
Runner
Author : Chanwit Settavongsin
"""
def main(text, number):
    """ Print text * n time """
    for _ in range(number):
        print(text)

main(input(), int(input()))
