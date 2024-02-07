'''
Object :

46.	Write a program to calculate the sum of the following series till the nth term
1/1! + 2/2! + 3/3! + 4/4! +…….+ n/n!

logic - for i in range(1,6):
    result = result * i
'''

num = int(input("Give the number of times you want to add : "))

result = 0
fact = 1
for i in range(1, num+1):
    fact = fact * i
    result = result + (i/fact)


print(result)