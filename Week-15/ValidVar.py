"""
ValidVar
Author : Chanwit Settavongsin
"""
def main(number, answer):
    """ print """
    for _ in range(number):
        answer.append(check(input().strip(" ")))
    print(*answer, sep="\n")

def check(word):
    """ Check variable name """
    keyword = ['if', 'else', 'elif', 'while', 'for', 'True', 'False', 'continue', 'break',\
    'return', 'is', 'in', 'and', 'or', 'from', 'as', 'pass', 'not', 'def', 'None']
    if word.isidentifier() and word not in keyword:
        answer = "Valid"
    else:
        answer = "Invalid"
    return answer

main(int(input()), [])
