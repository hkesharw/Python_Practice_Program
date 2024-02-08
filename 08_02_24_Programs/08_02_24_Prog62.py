'''

Object :

63.	Write a program that can create a new list from a given list where each item in the new list is square of the item of the old list

'''
import sys

y = 0
l1 = []
l2 = []

while True:

    if y == 1:
        for i in range(len(l1)):
            l2.append(l1[i]**2)
        print(f"Square of the old list elements are {l2}")
        sys.exit()

    else:
        l1.append(int(input("Enter the number : ")))
        y = int(input("Do you want to add more item if yes select any key otherwise select 1: "))


