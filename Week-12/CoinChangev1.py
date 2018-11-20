"""
CoinChangev1
Author : Chanwit Settavongsin
"""
def main(money):
    """ Find number of coin that to give """
    coin1, coin2 = divmod(money, 25)
    coin3, coin4 = divmod(coin2, 10)
    coin5, coin6 = divmod(coin4, 5)
    coin7 = coin6 // 1
    print(coin1 + coin3 + coin5 + coin7)

main(int(input()))
