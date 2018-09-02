"""
SceneSwitch I
Author: Woramat Ngamkham
"""
def light_switch(current_state="COOL", last_state="COOL", total_warm=0):
    """
    Find how many time to switch a light to warm light
    if we turn off and turn on within 6 seconds it will change
    state of light, otherwise it change to initial state (cool)

    Variables:
        current_state  (str): current state of light (CLOSE, COOL, WARM)
        last_state     (str): last state that light is on (COOL, WARM)
        init_time    (float): last time in seconds that switching
        diff_time    (float): detect time in seconds that switch had been switched
        total_warm     (int): total time that light change to warm light
    """

    try:
        init_time = float(input())
        while True:
            diff_time = float(input())
            if current_state != 'CLOSE':
                current_state = 'CLOSE'
                init_time = diff_time
            elif diff_time - init_time <= 6:
                current_state = 'WARM' if last_state == 'COOL' else 'COOL'
                last_state = current_state
                total_warm += 1 if current_state == 'WARM' else 0
            else:
                current_state, last_state = 'COOL', 'COOL'
    except ValueError:
        return total_warm

print(light_switch())