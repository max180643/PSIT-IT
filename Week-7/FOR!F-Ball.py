"""
FOR!F-Ball
Author : Chanwit Settavongsin
"""
def main(text, position):
    """ Find the last position of the glass. """
    for i in text:
        if i == "A" and position == 1: # A -> B
            position = 2
        elif i == "C" and position == 1: # A -> C
            position = 3
        elif i == "B" and position == 2: # B -> C
            position = 3
        elif i == "A" and position == 2: # B -> A
            position = 1
        elif i == "C" and position == 3: # C -> A
            position = 1
        elif i == "B" and position == 3: # C -> B
            position = 2
    print(position)

main(input(), 1)
