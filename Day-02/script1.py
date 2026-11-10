# syntax 01 [expression]  for variable in iterable ]

# nums =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = []
# for num in nums:
#     if num % 2 == 0:
#         result.append(num**2)
#     else:
#         result.append(num**3)
# print(result)

# # using list comprehension
# print([num **2 for num in nums])
# print([num **2 for num in nums if num % 2 == 0])
# print([num **2 for num in nums if num % 2 == 0 and num % 3 == 0])
# print([num **2 if num % 2 == 0 else num **3 for num in nums])

# lst = []
# for i in range(1, 11):
#     for j in range(1, 11):
#         lst.append(i * j)
# print(lst)

# print([i * j for i in range(1, 11) for j in range(1, 11)])


dICT = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
print({k: v for k, v in dICT.items()})