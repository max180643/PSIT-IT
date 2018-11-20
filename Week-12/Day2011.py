"""
Day2011
Author : Chanwit Settavongsin
"""
def main(date, month, number):
    """ What day from date and month in year 2011 """
    data = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    for i in range(month):
        number += data[i]
    answer = (number + date) % 7
    print("Saturday" if answer == 1 else "Sunday" if answer == 2 else "Monday"\
     if answer == 3 else "Tuesday" if answer == 4 else "Wednesday" if answer == 5\
      else "Thursday" if answer == 6 else "Friday")

main(int(input()), int(input()), 0)
