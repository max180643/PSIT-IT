"""
[EX] ClockHands
Author : Chanwit Settavongsin
"""
def main(hour, minute):
    """
    Hour and Minute hands of a Clock Superimposed Check
    hour = (0 <= hour < 12), minute = (0 <= minute < 60)
    if Superimposed print "True" else print "False"
    """
    if minute == int(5.45 * hour):
        print("True")
    else:
        print("False")

main(int(input()), int(input()))
