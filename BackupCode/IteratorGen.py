# num = [10,20,30]
# it = iter(num)
# print(next(it))
# print(next(it))
# print(next(it))

# class CountUpto:
#     def __init__(self,max):
#         self.max = max
#         self.current = 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current <= self.max:
#             value = self.current
#             self.current += 1
#             return value
#         else:
#             raise StopIteration

# for i in CountUpto(5):
#     print(i)


def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)