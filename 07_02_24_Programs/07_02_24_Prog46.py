'''

Object :

47.	Write a Python Program to Find the Sum of the Series till the nth term:
1 + x^2/2 + x^3/3 + … x^n/n
n will be provided by the user

'''

num = int(input("Enter the number : "))
result = 1
for i in range(1, num+1):

    result = result + num**(i+1)//(i+1)

print(result)
