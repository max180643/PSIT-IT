"""
Bill
Author : Chanwit Settavongsin
"""
def main(price, service, vat):
    """
    find price + service + vat
    Service 10% of price
    if Service < 50: Service = 50
       Service > 1000: Service = 1000
    Vat 7% of price + service
    """
    service = (price * 10)/100
    if service < 50:
        service = 50
    elif service > 1000:
        service = 1000
    price += service
    vat = (price * 7)/100
    price += vat
    print("%.2f" % (price))

main(int(input()), 0, 0)
