"""
WeightStation
Author : Chanwit Settavongsin
"""
def main():
    """
    Total weight more than 15000 kg, print "Overweight"
    Each weight will not more than or less than half of average, if not print Unbalance
    """
    # input
    avg1 = float(input())
    wheel_2 = float(input())
    wheel_3 = float(input())
    wheel_4 = float(input())
    # find wheel_1
    wheel_1 = avg1*4 - wheel_2 - wheel_3 - wheel_4
    # check & output
    if (wheel_1 + wheel_2 + wheel_3 + wheel_4) > 15000:
        print("Overweight")
    elif wheel_1 > (avg1 * 1.5) or wheel_2 > (avg1 * 1.5) or\
    wheel_3 > (avg1 * 1.5) or wheel_4 > (avg1 * 1.5) or\
    wheel_1 < (avg1 * 0.5) or wheel_2 < (avg1 * 0.5) or\
    wheel_3 < (avg1 * 0.5) or wheel_4 < (avg1 * 0.5):
        print("Unbalance")
    else:
        print("Pass %.2f" % (wheel_1))

main()
