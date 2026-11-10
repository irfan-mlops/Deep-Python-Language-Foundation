# Deep Copy 
from copy import deepcopy

list1 = [[2, 3], [4, 5]]

list2 = deepcopy(list1)

print("List1:", list1)
print("List2:", list2)

print(id(list1), id(list2))