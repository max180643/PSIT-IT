"""
HorizontalHistogram
Author : Chanwit Settavongsin
"""
def main(text, char_lower, char_upper, total_lower, total_upper):
    """ Print histogram of number's character """
    answer_char, answer_total = [], []
    _ = [char_lower.append(i) for i in text if i not in char_lower and i.islower()]
    _ = [char_upper.append(i) for i in text if i not in char_upper and i.isupper()]
    char_lower, char_upper = sorted(char_lower), sorted(char_upper)
    _ = [total_lower.append(text.count(i)) for i in char_lower]
    _ = [total_upper.append(text.count(i)) for i in char_upper]
    _ = answer_char.extend(char_lower), answer_char.extend(char_upper)
    _ = answer_total.extend(total_lower), answer_total.extend(total_upper)
    for i in range(len(answer_char)):
        total1, total2 = answer_total[i] // 5, answer_total[i] % 5
        print("%s : %s" % (answer_char[i], (("-----|" * total1 + "-" * total2).rstrip("|"))))

main(input(), [], [], [], [])
