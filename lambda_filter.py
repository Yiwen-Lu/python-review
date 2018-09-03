nums = [11, 22, 33, 44, 55]

is_even = list(map(lambda x: x % 2 == 0, nums)) # using map here to check nums, return Ture or False 
res = list(filter(lambda x: x % 2 == 0, nums))

print(is_even) # length: 5
print(res) # length: 2
