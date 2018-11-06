"""
Duplicate I
Author : Chanwit Settavongsin
"""
def main(num1, num2, data1, data2, answer):
    """ Find duplicate in list """
    _ = [data1.append(input()) for _ in range(num1)]
    _ = [data2.append(input()) for _ in range(num2)]
    if num1 > num2:
        _ = [answer.append(i) for i in data2 if i in data1]
    else:
        _ = [answer.append(i) for i in data1 if i in data2]
    answer.sort(reverse=True)
    if len(answer) > 0:
        _ = [print(i) for i in answer]
    else:
        print("Nope")

main(int(input()), int(input()), [], [], [])
