def find_adults(list_):
    adults = []
    for age in list_:
        if age >= 18:
            adults.append(age)
    return adults

list_ = [13, 24, 15, 18, 21, 30]
print(find_adults(list_))