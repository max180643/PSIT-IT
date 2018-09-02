"""
SceneSwitch I
Author : Chanwit Settavongsin
"""
def main():
    """ Warmlight Count """
    now_status = 1 # 0 = off, 1 = daylight, 2 = warmlight
    last_status = 1 # 1 = daylight, 2 = warmlight
    warm = 0 # answer
    start_time = input()
    if start_time != "End":
        while True:
            last_time = input()
            if last_time == "End":
                break
            elif now_status != 0:
                now_status = 0
                start_time = last_time
            elif float(last_time) - float(start_time) <= 6:
                if last_status == 1:
                    now_status = 2
                else:
                    now_status = 1
                last_status = now_status
                if now_status == 2:
                    warm += 1
            else:
                now_status = 1
                last_status = 1
    print(warm)

main()
