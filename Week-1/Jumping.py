"""
Jumping
Author : Chanwit Settavongsin
"""
def main():
    """ call function "show_text" 4 time """
    show_text("Output1")
    show_text("Output2")
    show_text("Output3")
    show_text("Output4")

def show_text(text):
    """Print text 3 time"""
    print("%s\n%s\n%s" % (text, text, text))

main()
