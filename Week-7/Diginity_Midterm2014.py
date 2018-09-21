"""
Diginity_Midterm2014
Author : Chanwit Settavongsin
"""
def main():
    """ loop sum each digit to 1 digit """
    ans = ""
    temp = 0
    while True:
        num = str(input())
        if num == "0":
            break
        while len(num) > 1:
            for i in num:
                temp += int(i)
            num = str(temp)
            temp = 0
        ans += "%s " % (num)
    print(ans.replace(" ", "\n"))

main()
