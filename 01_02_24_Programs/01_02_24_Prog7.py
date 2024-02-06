'''
Object - 7.	Write a program that will tell whether the given year is a leap year or not.
'''
year = int(input("Enter the year: "))

if year%4==0:
    print("Leap Year")
else:
    print("Not Leap Year")