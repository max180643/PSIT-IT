"""
NumDays
Author : Chanwit Settavongsin
"""
def main(frist_day, frist_month, second_day, second_month):
    """ Find day total """
    data = {
        1:31, 2:28, 3:31, 4:30,
        5:31, 6:30, 7:31, 8:31,
        9:30, 10:31, 11:30, 12:31
    }
    if frist_day <= data[frist_month] and second_day <= data[second_month]:
        if frist_month == second_month:
            print(max(frist_day, second_day) - min(frist_day, second_day))
        else:
            data1 = {}
            temp = 0
            data1[frist_month] = frist_day
            data1[second_month] = second_day
            data2 = sorted(data1)
            for i in range(data2[0]+1, data2[1]):
                temp += data[i]
            print(data[data2[0]] - data1[data2[0]] + data1[data2[1]] + temp)
    else:
        print("Impossible")

main(int(input()), int(input()), int(input()), int(input()))
