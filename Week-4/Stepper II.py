"""
Stepper II
Author : Chanwit Settavongsin
"""
def main(num_m, num_n):
    """ Print m to n """
    # Check
    if num_n < num_m:
        for i in range(num_m, num_n-1, -1):
            print(i)
    else:
        for i in range(num_m, num_n+1):
            print(i)

main(int(input()), int(input()))
