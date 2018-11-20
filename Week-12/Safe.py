"""
Safe
Author : Chanwit Settavongsin
"""
def main(display, password, answer):
    """ Counts the number of times the code is rotated. """
    for i in range(len(display)):
        different = abs(ord(display[i]) - ord(password[i]))
        if different > 13:
            answer += 26 - different
        else:
            answer += different
    print(answer)

main(input(), input(), 0)
