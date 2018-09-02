from itertools import accumulate, takewhile

nums = list(accumulate(8)) # add up from 0 to 7
print(nums)
print(list(takewhile(lambda x: x <= 6, nums))) # equivalent to filter
