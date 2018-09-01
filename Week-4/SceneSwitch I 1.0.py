"""
SceneSwitch I
Author : Chanwit Settavongsin
"""
def main():
    """ Warmlight Count """
    count = 0
    daylight = input()
    while True:
        if daylight == "End":
            break
        lightoff = input()
        if lightoff == "End":
            break
        warmlight = input()
        if warmlight == "End":
            break
        if float(warmlight) - float(lightoff) <= 6:
            count += 1
            lightoff = input()
            if lightoff == "End":
                break
            daylight = input()
    print(count)

main()
