"""
VerticalHistogram
Author : Chanwit Settavongsin
"""
def main(text, char_lower, char_upper, total_lower, total_upper):
    """ Print histogram of number's character """
    answer_char, answer_total, answer = [], [], {}
    _ = [char_lower.append(i) for i in text if i not in char_lower and i.islower()]
    _ = [char_upper.append(i) for i in text if i not in char_upper and i.isupper()]
    char_lower, char_upper = sorted(char_lower), sorted(char_upper)
    _ = [total_lower.append(text.count(i)) for i in char_lower]
    _ = [total_upper.append(text.count(i)) for i in char_upper]
    _ = answer_char.extend(char_lower), answer_char.extend(char_upper)
    _ = answer_total.extend(total_lower), answer_total.extend(total_upper)
    max_total = max(answer_total)
    for i in range(len(answer_char)):
        answer[answer_char[i]] = answer_total[i]
    for i in range(max_total, -1, -1):
        if i == 0:
            print("   ", end=" ")
            for i in answer_char:
                print(i, end=" ")
        else:
            print("%03d" % (i), end=" ")
            for j in range(len(answer_char)):
                if i == answer[answer_char[j]]:
                    print("*", end=" ")
                    answer[answer_char[j]] -= 1
                else:
                    print(" ", end=" ")
            print()

main(input(), [], [], [], [])
