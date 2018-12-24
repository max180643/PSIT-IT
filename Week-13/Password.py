"""
Password
Author : Chanwit Settavongsin
"""
import hashlib
def main(text):
    """ Hashing SHA512 """
    hashing = hashlib.sha512(text.encode())
    print(str(hashing.hexdigest()).upper())

main(input())
