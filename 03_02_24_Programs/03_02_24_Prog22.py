'''
Object :
23.	Write a program that will swap numbers
'''

num1 = int(input("Enter the number 1 : "))
num2 = int(input("Enter the number 2: "))

num1 = num1 + num2
num2 = num1 - num2
num1 = num2 - num1

if num1 < 0:
    print(f"Number is Swapped now number1= {-num1} and number2={num2}")
if num2 < 0:
    print(f"Number is Swapped now number1= {num1} and number2={-num2}")
