"""Key_Midterm2014"""
def main(id_number, value1, value):
    """
    find value
    condition : 1.find sum of number
                2.last 3 digit multiply 10
                3.value = value1 + value2
                if digit of value > 4 pick only 4 last digit
                   digit of value < 4 add 1000 to value
    """
    for i in id_number:
        value1 += int(i)
    value2 = int(id_number) % 1000 * 10
    value = value1 + value2
    if value >= 10000:
        value %= 1000
    elif value < 1000:
        value += 1000
    print("%04i" % (value))

main(input(), 0, 0)
