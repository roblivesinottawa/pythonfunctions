def get_evens(_list):
    evens = []
    for n in _list:
        if n % 2 == 0:
            evens.append(n)
    return evens

_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_evens(_list))