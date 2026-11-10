# # for loop for table of a number
# number = int(input("Enter a number to print its multiplication table: "))
# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")

# import sys
# import demo
# print(demo.add(5, 3))
# print(sys.path)

# import json
# # enumerate function

# sports = ["cricket", "football", "basketball", "tennis"]
# enum_sports = enumerate(sports)
# print(enum_sports)# Convert to list to see the enumerated pairs
# data = dict(list(enumerate(sports)))
# f =  open("sports.json", "w")
# json.dump(data, f)
# f.close()
# for index, sport in enumerate(sports):
#     print(f"Index: {index}, Sport: {sport}")

# # dictionary with enumerate
# student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
# for index, (student, score) in enumerate(student_scores.items()):
#     print(f"Index: {index}, Student: {student}, Score: {score}")



import copy
original_list = [1, 2, [3, 4]]
new_list = copy.copy(original_list)  # Shallow copy
new_list[2][0] = 99  # Modifying the nested list in the
print("Original List:", original_list)  # Output: [1, 2, [99, 4]]