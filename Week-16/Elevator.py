"""
Elevator
Author : Chanwit Settavongsin
"""
def main(total_floor, now_floor):
    """ Find floor that elevator stop """
    answer = now_floor
    while True:
        command = input()
        if command == "END":
            break
        elif command == "UP" and answer != total_floor:
            answer += 1
        elif command == "DOWN" and answer != 1:
            answer -= 1
    print(answer)

main(int(input()), int(input()))
