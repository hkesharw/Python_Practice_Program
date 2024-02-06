'''
Object:

13.	Write  a program that will tell whether the given number is divisible by 3 & 6.
'''
num = int(input("Enter number : "))

if num%3==0 and num%6==0:
    print("Given number is divisible by 3 and 6")
else:
    print("Not divisible by 3 and 6")