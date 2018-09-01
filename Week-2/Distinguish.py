"""
Distinguish
Author : Chanwit Settavongsin
"""
def main(height):
    """
    Check Height
    height > 180 ; print "You're hit the door edge."
    height <= 180 ; print "Nothing happens."
    """
    print("You're hit the door edge." if height > 180 else "Nothing happens.")

main(int(input()))
