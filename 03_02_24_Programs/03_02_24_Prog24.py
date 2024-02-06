'''
Object :

25.	Write a program that can multiply 2 numbers provided by the user without using the * operator
'''

num1 = int(input("Enter the number1 : "))
num2 = int(input("Enter the number2 : "))

k = 0
for i in range(num2):
    k = k + num1

print(k)
