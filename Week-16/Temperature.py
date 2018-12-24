"""
Temperature
Author : Chanwit Settavongsin
"""
def main(temp, unit_form, unit_to):
    """ Convert temperature from this unit to another unit """
    celsius_ans = celsius(temp, unit_form)
    if unit_to == "C":
        answer = celsius_ans
    elif unit_to == "F":
        answer = celsius_ans * 9 / 5 + 32
    elif unit_to == "K":
        answer = celsius_ans + 273.15
    elif unit_to == "R":
        answer = (celsius_ans + 273.15) * 9 / 5
    return answer

def celsius(temp, unit):
    """ Convert any temperature to celsius """
    if unit == "C":
        temp_ans = temp
    elif unit == "F":
        temp_ans = (temp - 32) * 5 / 9
    elif unit == "K":
        temp_ans = temp - 273.15
    elif unit == "R":
        temp_ans = (temp - 491.67) * 5 / 9
    return temp_ans

print("%.2f" % (main(float(input()), input(), input())))
