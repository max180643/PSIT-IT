"""
TheFunctionWithin
Author : Chanwit Settavongsin
"""
def main():
    """ Call equation function and Print output """
    var_a = float(input())
    var_b = float(input())
    var_c = float(input())
    var_d = float(input())
    print(var_f(var_f(var_a)))
    print(var_g(var_f(var_a-var_b)))
    print(var_h(var_f(var_a+var_b), var_f(var_a+var_c), var_g(var_f(var_d**2))))
    print(var_i(var_h(var_f(var_a+var_b), var_f(var_a-var_c), var_g(var_f(var_d**2)))\
        , var_g(var_f(var_a-var_b))\
        , var_f(var_f(var_f(var_f(var_f(var_c)))))\
        , var_d**8))

def var_f(num):
    """ find f value """
    return 2*num

def var_g(num):
    """ find g value """
    return 3*num**4 - num**3 + 2*num**2 + 10

def var_h(num1, num2, num3):
    """ find h value """
    return (num3+num1)**2 - num1*num2 + num2**2

def var_i(num1, num2, num3, num4):
    """ find i value"""
    return (num1**2 + num2**2 - num3**2) / (num4**2 - 2*num1*num4 + 2*num1)

main()
