"""
Flatten
Author : Chanwit Settavongsin
"""
import json
def main(text, answer):
    """ Remove all list and store in one list """
    for item in text:
        if isinstance(item, list):
            text.extend(item)
        else:
            answer.append(item)
    answer.sort(reverse=True)
    print(answer)

main(json.loads(input()), [])
