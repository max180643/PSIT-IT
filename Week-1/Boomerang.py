"""Boomerang"""
def main(x_var, y_var, z_var):
    """Print Number"""
    print(x_var+1)
    print(7*y_var**3 + 2*y_var**2 - 31*y_var +1)
    print(0 - z_var)
    print((x_var+y_var)*(x_var-y_var))
    print((y_var - ((y_var**2 - 4*x_var*z_var)**(1/2)))/(2*x_var))

main(int(input()), int(input()), int(input()))
