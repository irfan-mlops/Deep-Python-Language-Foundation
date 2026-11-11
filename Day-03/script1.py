# def total_cost(items, currency= "USD"):
#     total = sum(items.values())
#     print("Total cost is :", total, currency)

# cart ={ "apple": 2.5, "banana": 1.2, "orange": 3.0}
# total_cost(items=cart, )  # Using default tax 
# print(total_cost.__defaults__)




# def add_item(name, emplyee_id=[]):
#     emplyee_id.append(name)
#     print(f"update employee list: {emplyee_id}")

# add_item("John")
# print(add_item.__defaults__)  # prints the default value of emplyee_id
# add_item("Alice")
# print(add_item.__defaults__)  # prints the updated default value of emplyee_id

# variable-length positional Arguments

# def addition(**nums):
#     print(nums.values())
# print(addition(n1=10,n2=20,n3=30))


# mixing variable length keyword and positional arguments

# def addition (*num, **nums):
#     print(num)
#     print(nums)

# print(addition(100,200,3000, n1= 100, n2=200, n3=400))