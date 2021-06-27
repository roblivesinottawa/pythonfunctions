list_nums = [10, 34, 85, 78, 21, 87, 190, 235, 400]

get_evens = list(filter(lambda x : x % 2 == 0, list_nums))

print(f"The Even Numbers are: {get_evens}")