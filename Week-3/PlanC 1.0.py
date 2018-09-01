"""
PlanCDEFGHIJKLMNOPQRSTUVWXYZ
Author : Chanwit Settavongsin
"""
def top(in1, in2):
    """ M.ax Function """
    output = 0
    if in1 > in2:
        output = in1
    else:
        output = in2
    return output

def low(in1, in2):
    """ M.in Function """
    output = 0
    if in1 < in2:
        output = in1
    else:
        output = in2
    return output

def main(text, num1, num2, num3):
    """
    S.ort Function 
    text = "Ascend" ; s.ort m.in to m.ax and print
    text = "Descend" ; s.ort m.ax to m.in and print
    """
    if text == "Ascend":
        # loop1
        num1, num2 = low(num1, num2), top(num1, num2)
        num2, num3 = low(num2, num3), top(num2, num3)
        # loop2
        num1, num2 = low(num1, num2), top(num1, num2)
        num2, num3 = low(num2, num3), top(num2, num3)
    elif text == "Descend":
        # loop1
        num2, num3 = top(num2, num3), low(num2, num3)
        num1, num2 = top(num1, num2), low(num1, num2)
        # loop2
        num2, num3 = top(num2, num3), low(num2, num3)
        num1, num2 = top(num1, num2), low(num1, num2)
    print("%.2f, %.2f, %.2f" % (num1, num2, num3))

main(input(), float(input()), float(input()), float(input()))
