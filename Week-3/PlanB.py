"""
PlanB
Author : Chanwit Settavongsin
"""
def main(score):
    """
    Check Score
    score >= 450 ; Print "Pass"
    score < 450 ; Print "Fail"
    """
    print("Pass" if score >= 450 else "Fail")
    print("Process is terminated")

main(float(input()))
