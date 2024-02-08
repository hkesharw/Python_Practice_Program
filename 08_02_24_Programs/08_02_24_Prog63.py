'''

Object :

64.	Write a program that can reverse words of a given string (by using list).
Eg - if the input is : Hello how are you
Output should be : you are how Hello

'''
import sys

y = 0
l1 = []
l2 = []
while True:
    if y == 1:
        k = len(l1) - 1
        for i in range(k, -1, -1):
            l2.append(l1[i])
        print(l1)
        print(l2)
        sys.exit()
    else:
        l1.append(input("Enter the words : "))
        y = int(input("Want to add more element press any key within 0-9 otherwise press 1 : "))
