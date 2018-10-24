"""
Classify
Author : Chanwit Settavongsin
"""
def main(text, data, temp):
    """ Show information of year, faculty, member """
    while text != "END":
        text = input()
        if text[:4] not in data and text != "END":
            data[text[:4]] = 1
        elif text[:4] in data and text != "END":
            data[text[:4]] += 1
    for i in sorted(data):
        if i[:2] != temp:
            print(i[:2], int(i[2:4]), data[i])
        else:
            print("--", int(i[2:4]), data[i])
        temp = i[:2]

main("", {}, "")
