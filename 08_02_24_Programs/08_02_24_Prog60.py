'''

Object :

61.	Write a python program to reverse a list

'''
import sys

l1 = []
y = 0
l2 = []
while True:
    if y == 1:
        k = len(l1)
        print("Reversed list will be like this ", end='')
        for i in range(k, 0, -1):
            l2.append(l1[i-1])
        print(l2)
        sys.exit()
    else:
        l1.append(input("Enter the element you want to add in the list : "))
        y = int(input("Select 1 to exit or select any key add more ele in the list : "))
