"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def main(text, num1, num2, num3):
    """S.ort"""
    num_1, num_2 = num_1 if num_1 < num_2 else num_2, num_1 if num_1 > num_2 else num_2
    num_1, num_3 = num_1 if num_1 < num_3 else num_3, num_1 if num_1 > num_3 else num_3
    num_2, num_3 = num_2 if num_2 < num_3 else num_3, num_2 if num_2 > num_3 else num_3

    if text == "Ascend":
        print("%.2f, %.2f, %.2f" % (num1, num2, num3))
    elif text == "Descend":
        print("%.2f, %.2f, %.2f" % (num3, num2, num1))

main(input(), float(input()), float(input()), float(input()))
