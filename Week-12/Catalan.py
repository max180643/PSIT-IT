"""
Catalan
Author : Chanwit Settavongsin
"""
def main(number):
    """ Number of catalan """
    if number in (1, 2):
        return number
    else:
        number -= 1
    return int((4 * number + 2)/(number + 2) * main(number))

print(main(int(input())))
