"""
MacaronBoxSML
Author : Chanwit Settavongsin
"""
def main(number):
    """ Calculate box used """
    large, total = divmod(number, 24)
    print(int(total > 0 and total <= 6),\
    int(total > 6 and total <= 12),\
    int(total > 12) + large, sep='\n')

main(int(input()))
