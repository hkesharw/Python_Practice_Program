'''
Object - 9.	Write a program that take a user input of three angles and will find out whether it can form a triangle or not.

formulae - a+b>c, b+c>a,a+c>b
'''

side1 = int(input("Enter side1 : "))
side2 = int(input("Enter side2 : "))
side3 = int(input("Enter side3 : "))

if side1+side2>side3 and side2+side3>side1 and side3+side1>side2:
    print("Yes it is a triangle")
else:
    print("Not a triangle")
