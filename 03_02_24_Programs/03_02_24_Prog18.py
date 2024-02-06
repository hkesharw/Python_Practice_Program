'''
Onject:

18.	Write a program that will check whether the number is armstrong number or not.

'''

a = input("Enter the number : ")
x = int(a)
k = len(a)
j = 0
for i in range(k):
    m = int(a[i])
    j = j + m ** k

if x == j:
    print("Armstrong number")
else:
    print("Not Armstrong number")
