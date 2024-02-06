'''
Object :

26.	Write a program that can find the factorial of a given number provided by the user.

'''

number = int(input("Enter the number : "))
k =1
for i in range(number):
    k = k + k*i

print(k)