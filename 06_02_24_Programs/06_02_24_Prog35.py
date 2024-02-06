'''

Object :

36.	Write a program to find the compound interest

'''

principle = float(input("Enter the principle amount : "))

rate = float(input("Enter rate : "))

time = int(input("Enter time : "))

amount = principle*(1+rate/100)**time

ci = amount - principle

print(f"Total Compount Intrest is {ci}")


