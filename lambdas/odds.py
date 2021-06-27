list_nums = [10, 34, 85, 78, 21, 87, 190, 235, 400]

get_odds = list(filter(lambda x : x % 2 != 0, list_nums))

print(f"The Odd Numbers are: {get_odds}")