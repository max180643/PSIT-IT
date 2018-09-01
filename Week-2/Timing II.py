"""
Timing II
Author : Chanwit Settavongsin
"""
def main():
    """
    Convert input number to 
    day, hour, minute, second and check 
    if day digit > 5 : print ("ERR_:__:__:__")
    else: print day, hour, minute, second
    """
    second = int(input())
    if second >= 0:
        minute, second = divmod(second, 60)
        hour, minute = divmod(minute, 60)
        day, hour = divmod(hour, 24)
        if day < 10000 and day >= 0:
            print("%04d:%02d:%02d:%02d" %(day, hour, minute, second))
        else:
            print("ERR_:__:__:__")
    else:
        print("ERR_:__:__:__")

main()
