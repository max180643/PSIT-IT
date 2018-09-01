"""
SurprisingVote
Author : Chanwit Settavongsin
"""
def main(total, top):
    """
    Check in these score can have difference more than 2
    by giving highest score and total score
    """
    # find low
    if top * 2 <= total:
        low = total - (top * 2)
    else:
        low = total - top
    # check
    print("Surprising" if abs(top -low) > 2 else "Not surprising")

main(float(input()), float(input()))
