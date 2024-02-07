'''

Object :

50.	Write a program that accepts 2 numbers from the user a numerator and a denominator and then simplifies it

Eg if the num = 5, den = 15 the answer should be ⅓
Eg if the num = 6, den = 9 the answer should be ⅔

'''
import sys

num = int(input("Enter the numerator : "))
deno = int(input("Enter the denominator : "))
i = 2
while True:
    if num % i == 0 and deno % i == 0:
        perfect_division = i
        num = num//perfect_division
        deno = deno//perfect_division
        print(f"The output of this program {num}/{deno}")
        sys.exit()
    elif num >= num or deno >= deno:
        print("The both number won't be divided by single value")
        sys.exit()
    else:
        i = i+1

