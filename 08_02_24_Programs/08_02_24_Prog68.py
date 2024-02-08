'''

Object :

68.	Write a program to merge 2 list without using the + operator

'''
from typing import List

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = []
for i in l1:
    l3.append(i)
for i in l2:
    l3.append(i)

print(f"list 1 {l1}")
print(f"list 2 {l2}")
print(f"New list is created without using + operator is {l3}")