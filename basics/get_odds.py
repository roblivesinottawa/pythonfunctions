def get_odds(_list):
    odds = []
    for x in _list:
        if x % 2 != 0:
            odds.append(x)
    return odds

_list = [20, 45, 64, 36, 92, 89, 32, 99]
print(get_odds(_list))