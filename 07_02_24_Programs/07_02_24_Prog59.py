'''

Object :

60.	Write a python program to find the max item from a list without using the max function

'''
import sys

y = 0
l1 = []
mx = 0

while True:
    if y == 1:
        for i in range(len(l1)-1):
            if l1[i] > l1[i+1]:
                mx = l1[i]
            else:
                mx = l1[i+1]
        print(f"The biggest number in the list is {mx}")
        sys.exit()
    else:
        l1.append(int(input("Enter the number you want to add in the list : ")))
        y = int(input("Do you want to add more item in list if yes then press 0 otherwise press 1 : "))


