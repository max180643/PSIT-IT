"""
Roman
Author : Chanwit Settavongsin
"""
def main(text, answer):
    """ Roman numeral to integer """
    number = text.replace('CM', '900 ').replace('M', '1000 ').replace('CD', '400 ')\
          .replace('D', '500 ').replace('XC', '90 ').replace('C', '100 ')\
          .replace('XL', '40 ').replace('L', '50 ').replace('IX', '9 ')\
          .replace('X', '10 ').replace('IV', '4 ').replace('V', '5 ').replace('I', '1 ')
    number = number.split()
    for i in number:
        answer += int(i)
    print(answer)

main(input(), 0)
