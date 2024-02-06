'''

Object :

28.	Write a program to print whether a given number is prime number or not

'''
import sys

num = int(input("Enter the number : "))

k = num//2

if num==1:
    print("Prime number")
for i in range(2,k+1):
    if num%i==0:
        print("Not a prime number")
        sys.exit()
    else:
        print("Prime number")
        sys.exit()