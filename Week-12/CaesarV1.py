"""
CaesarV1
Author : Chanwit Settavongsin
"""
def main(number, text, answer):
    """ Caesar Cipher decode """
    for i in text:
        char = ord(i)
        char += number % 26
        if i.isupper():
            if char < ord("A"):
                char += 26
            elif char > ord("Z"):
                char -= 26
            answer += chr(char)
        elif i.islower():
            if char < ord("a"):
                char += 26
            elif char > ord("z"):
                char -= 26
            answer += chr(char)
        else:
            answer += i
    print(answer)

main(int(input()), input(), "")
