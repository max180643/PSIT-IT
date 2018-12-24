"""
BreakPassword
Author : Chanwit Settavongsin
"""
import hashlib
def main(text):
    """ Hashing SHA512 """
    for number in range(0, 100000):
        value = str("%05d" % (number))
        hashing = hashlib.sha512(value.encode())
        if str(hashing.hexdigest()).upper() == text:
            print(str("%05d" % (number)))

main(input())
