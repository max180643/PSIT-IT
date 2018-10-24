"""
Filter
Author : Chanwit Settavongsin
"""
import json
def main(text, score, answer):
    """ Print id and score that greater-than or equal to score """
    text = json.loads(text)
    text = sorted(text.items()) # return tuple in list and sort key
    _ = [answer.append("%i#%.2f" % (int(i[0]), i[1])) for i in text if i[1] >= score]
    if len(answer) > 0:
        for i in answer:
            print(i.replace("#", "\t"))
    else:
        print('Nope')

main(input(), float(input()), [])
