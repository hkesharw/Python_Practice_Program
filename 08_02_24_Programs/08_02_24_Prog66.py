'''

Object :

66.	Write a program to check if a list is in ascending order or not

'''
import sys

y = 'a'
l1 = []
count = 0
while True:
    if y == 'n':
        for i in range(len(l1)-1):
            if l1[i] <= l1[i+1]:
                count = count + 1
        if count+1 == len(l1):
            print("Lists are ascending order")
            sys.exit()
        else:
            print("List are not in ascending order")
            sys.exit()
    else:
        l1.append(int(input("Enter the element you want to add in the list : ")))
        y = input("Enter Y if you add more element otherwise enter n: ")

