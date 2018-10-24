"""
AlmostMean
Author : Chanwit Settavongsin
"""
def main(total, data, avg, answer):
    """ Find who almostMean """
    for _ in range(total): # store data
        temp = input().split("\t")
        data[temp[0]] = temp[1]
    for j in data: # find average
        avg += float(data[j])
    avg = avg / total
    value = avg
    for k in data: # find nearest number
        if float(data[k]) < avg and (avg - float(data[k]) < value):
            value = avg - float(data[k])
            answer = k
    print("%s\t%s" % (answer, data[answer]))

main(int(input()), {}, 0, "")
