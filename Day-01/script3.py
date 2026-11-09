# if True:
#     print("Hello, World!")

# print("My name is John Doe.")


# # input and output functions Even function

# number = int(input("Enter a number: "))

# if number % 2 == 0: print("The number is even.")

# else: print("The number is odd.")

# # Nested if statement
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are an adult.")
#     if age >= 65:
#         print("You are a senior citizen.")
#     else:
#         print("You are not a senior citizen.")
# else:
#     print("You are a minor.")

# # IF-elif-else statement
# marks = int(input("Enter your marks: "))
# if marks >= 90:
#     print("You got an A grade.")
# elif marks >= 80:
#     print("You got a B grade.")
# elif marks >= 70:
#     print("You got a C grade.")
# else:
#     print("You need to work harder.")



# # While loop with else statement
# # user input for the number of table
# number = int(input("Enter a number to print its multiplication table: "))
# count = 1
# while count <= 10:
#     print(f"{number} x {count} = {number * count}")
#     count += 1
# else:
#     print("Multiplication table completed.")

# ## Nested while loop statement
# # user input for the number of table
# number = int(input("Enter a number to print its multiplication table: "))
# rows = int(input("Enter the number of rows for the pattern: "))
# count = 1
# while count <= rows:
#     inner_count = 1
#     while inner_count <= count:
#         print(f"{number} x {inner_count} = {number * inner_count}")
#         inner_count += 1
#     print()  # Print a new line after each row
#     count += 1

# While loop with range function
# # user input for the number of table
# number = int(input("Enter a number to print its multiplication table: "))
# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")

# print(list(range(2,10)))  # Print a new line after the table


# # For loop statement

# name = input("Enter your name: ")
# for char in name:
#     print(char)

# lsit1 =  ["apple", "banana", "cherry"]
# for fruit in lsit1:
#     print(fruit)
#     if fruit == "banana":
#         break  # Exit the loop when "banana" is found


# break statement in a while loop
count = 1
while count <= 10:
    if count == 5:
        break  # Exit the loop when count is 5
    print(count, end=" ")
    count += 1

# For loop with continue statement
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i, end=" ")
    
