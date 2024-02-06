'''
Object - User will input (3ages).Find the oldest one
'''
import sys
age1 = input("enter first age : ")
age2 = input("enter second age : ")
age3 = input("enter third age : ")

if age1==age2 and age2==age3:
    print("Same age for all")
    sys.exit()
if age1>=age2 and age1>=age3:
    print("the oldest age is", age1)
elif age2>=age1 and age2>=age3:
    print("The oldest age is", age2)
elif age3>=age2 and age3>=age1:
    print("the oldest age is", age3)