'''

Object :

39.	Print all factors of a given number provided by the user.

'''

num = int(input("Enter the number : "))

k = num // 2
l1 = []
for i in range(1, k+1):

    if num % i == 0:
        l1.append(i)

l1.append(num)
print(l1)