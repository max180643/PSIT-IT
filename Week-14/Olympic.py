"""
Olympic
Author : Chanwit Settavongsin
"""
def main(number, rank_dict, rank):
    """ Print scoreboard """
    for _ in range(number):
        country, gold, silver, bronze = input().split()
        key = int(gold), int(silver), int(bronze)
        countries = rank_dict.get(key, [])
        countries.append(country)
        rank_dict[key] = sorted(countries)
    for key in sorted(rank_dict, reverse=True):
        for cty in rank_dict[key]:
            print(rank, cty, key[0], key[1], key[2], sum(key))
        rank = rank + len(rank_dict[key])

main(int(input()), {}, 1)
