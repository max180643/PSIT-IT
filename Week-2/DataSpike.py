"""
DataSpike
Author : Chanwit Settavongsin
"""
def main(number, temp, count):
    """ Find Max Value """
    if count < 8:
        if number > temp:
            temp = number
        main(int(input()), temp, count + 1)
    else:
        if number > temp:
            temp = number
        print(temp)

main(int(input()), 0, 1)
