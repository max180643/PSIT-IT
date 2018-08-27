"""Distinguish"""
def main(height):
    """Check Height"""
    print("You're hit the door edge." if height > 180 else "Nothing happens.")

main(int(input()))
