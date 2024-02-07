'''

Object :

58.	Write a python program to remove all the duplicates from a list

'''
import sys

y = 3
l1 = []
while True:

    if y == 1:
        k = set(l1)
        j = list(k)
        print(f"Unique element are {j}")
        sys.exit()
    else:
        l1.append(input("Enter element : "))
        y = int(input("Do you want to add more element in the list if yes then select anything otherwise select 1: "))

