'''

Object :

37.	Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

'''

n = input("Enter the value of n : ")

k1 = int(n)

k2 = n + n
k2 = int(k2)
k3 = n + n + n
k3 = int(k3)

print(k1+k2+k3)
