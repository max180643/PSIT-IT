"""
SceneSwitch I
Author : Chanwit Settavongsin
"""
def main(text):
    """Warmlight Count"""
    light = 1 # 0 = off, 1 = on 
    mode = 0 # 0 = daylight, 1 = warmlight
    warm = 0 # answer 
    temp = 0 # old time
    while text != "End":
        time = input()
        if light != 0:
            light = 0
            temp = time
        elif time - temp <= 6:
            

        

main(input())