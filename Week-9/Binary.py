"""
Binary
Author : Chanwit Settavongsin
"""
def main(number, answer):
    """ Convert decimal to binary """
    if number > 0:
        while number != 0:
            number, temp = divmod(number, 2)
            answer.append(temp)
        answer.reverse()
        _ = [print(i, end="") for i in answer]
    else:
        print(number)

main(int(input()), [])
