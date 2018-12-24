"""
ProgressiveTax
Author : Chanwit Settavongsin
"""
def main(num):
    """ Tax Calculate """
    step1 = min(max(num - 150000, 0), 150000)
    step2 = min(max(num - 300000, 0), 200000)
    step3 = min(max(num - 500000, 0), 250000)
    step4 = min(max(num - 750000, 0), 250000)
    step5 = min(max(num - 1000000, 0), 1000000)
    step6 = min(max(num - 2000000, 0), 2000000)
    step7 = max(num - 4000000, 0)
    print(int(step1*0.05 + step2*0.10 + step3*0.15 + step4*0.20 \
          + step5*0.25 + step6*0.30 + step7*0.35))

main(int(input()))
