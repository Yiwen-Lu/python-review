nums = [11, 22, 33, 44, 55]

check = list(map(lambda x: x % 2 == 0, nums))
res = list(filter(lambda x: x % 2 == 0, nums))

print(check)
print(res)