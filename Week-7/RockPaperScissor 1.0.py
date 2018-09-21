"""
RockPaperScissor
Author : Chanwit Settavongsin
"""
def main(text, score_a, score_b):
    """
    Condition : Count Score
                temp[0] = player a
                temp[1] = player b
    """
    start = 0
    stop = 0
    for i in range(2, len(text) + 1, 2):
        stop = i
        temp = text[start:stop]
        if temp[0] == "P" and temp[1] == "R":
            score_a += 1
        elif temp[0] == "R" and temp[1] == "P":
            score_b += 1
        elif temp[0] == "S" and temp[1] == "P":
            score_a += 1
        elif temp[0] == "P" and temp[1] == "S":
            score_b += 1
        elif temp[0] == "R" and temp[1] == "S":
            score_a += 1
        elif temp[0] == "S" and temp[1] == "R":
            score_b += 1
        start = stop
    if score_a > score_b:
        print("A win %i-%i" % (score_a, score_b))
    elif score_b > score_a:
        print("B win %i-%i" % (score_b, score_a))
    else:
        print("DRAW %i" % (score_a))

main(input(), 0, 0)
