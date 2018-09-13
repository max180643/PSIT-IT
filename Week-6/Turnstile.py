"""
Turnstile
Author : Chanwit Settavongsin
"""
def main(status, count):
    """ Count people pass this turnstile """
    while True:
        command = input()
        if command == "END":
            break
        elif command == "C":
            status = "unlock"
        elif command == "P" and status == "unlock":
            count += 1
            status = "lock"
    print(count)

main("lock", 0)
