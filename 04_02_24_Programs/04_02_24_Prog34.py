'''

Object :

1.	Print the first 20 numbers of a Fibonacci series

'''

a = 0
b = 1
s = 0

for i in range(26):
    print(s,end=' ')
    s = a+b
    b = a
    a = s
