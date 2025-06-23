# lambda args:expression

# add = lambda x,y: x+y
# print(add(10,20))

# def add_func(x,y):
#     return x + y
# print(add_func(10,20))

# nums = [1, 2, 3, 4, 5]
# # squared_nums = list(map(function,iteration))
# add = list(map(lambda x: x+2, nums))
# print(add)

# nums = [1, 2, 3, 4, 5]
# evens = list(filter(lambda x: x % 2 == 0, nums))
# print(evens)

# nums = [1, 2, 3, 4]
# product = 1
# for num in nums:
#     product = product * num
# print(product)

from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)
