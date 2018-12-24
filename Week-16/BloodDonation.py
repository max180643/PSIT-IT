"""
BloodDonation
Author : Chanwit Settavongsin
"""
def main(age, weight, time, answer):
    """ BloodDonation check """
    if age == 17 or (age >= 60 and age <= 70):
        cert = input()
        if age >= 17 and age <= 70 and weight >= 45 and \
        (time > 0 or (time == 0 and age <= 55)) and cert == "True":
            answer = "Yes"
    elif age >= 17 and age <= 70 and weight >= 45 and (time > 0 or (time == 0 and age <= 55)):
        answer = "Yes"
    return answer

print(main(int(input()), int(input()), int(input()), "No"))
