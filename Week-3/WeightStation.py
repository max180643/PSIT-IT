"""WeightStation"""
def main():
    """Check Weight"""
    # input
    avg1 = float(input())
    wheel_2 = float(input())
    wheel_3 = float(input())
    wheel_4 = float(input())
    # find wheel_1
    wheel_1 = avg1*4 - wheel_2 - wheel_3 - wheel_4
    # check & output
    temp = avg1 / 2
    if (wheel_1 + wheel_2 + wheel_3 + wheel_4) > 15000:
        print("Overweight")
    elif temp < (avg1 - wheel_1) or temp < (avg1 - wheel_2) or\
     temp < (avg1 - wheel_3) or temp < (avg1 - wheel_4):
        print("Unbalance")
    else:
        print("Pass %.2f" % (wheel_1))

main()
