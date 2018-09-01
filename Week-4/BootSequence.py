"""
BootSequence
Author : Chanwit Settavongsin
"""
def main(number):
    """ Print 1_2_3 .... _n """
    for i in range(1, number):
        print("%i_" % (i), end="")
    print(number)

main(int(input()))
