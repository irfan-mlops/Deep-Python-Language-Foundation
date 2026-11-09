# Variables and Datatypes
print(bin(4)) # Binary representation of 4
print(oct(4)) # Octal representation of 4
print(hex(4)) # Hexadecimal representation of 4
print(5<<4) # left shift Operator
print(5>>4) # right shift Operator

# -------------------------------------------------------------------------

# data types
x = 5 # int
print(type(x)) # prints the type of x
x = 5.0 # float
print(type(x)) # prints the type of x
x = 5 + 3j # complex
print(type(x)) # prints the type of x

#=========================================================================

a =  "Hello" # string
print(type(a)) # prints the type of a

b = [1, 2, 3, 4] # list
print(type(b)) # prints the type of b

c = (1, 2, 3, 4) # tuple
print(type(c)) # prints the type of c

d = {1, 2, 3, 4} # set
print(type(d)) # prints the type of d

e = {'name': 'John', 'age': 30} # dictionary
print(type(e)) # prints the type of e

f = True # boolean
print(type(f)) # prints the type of f


#------------------------------------------------------------------------

#Indexing and Slicing

a = "Hello, World!" # string
print(a[0]) # prints the first character of a
print(a[7:12:2]) # prints the substring from index 7 to 11

#-------------------------------------------------------------------------
#Type Conversion
A = 5 # int
B = str(2.5) # float
print(str(A)) # converts int to string
print(type(B)) # converts float to int


#-----------------------------------------------------------------------

