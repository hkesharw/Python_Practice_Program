'''

Object :

45.	Write a program to print the following pattern
1
2 3
4 5 6
7 8 9 10

'''
k = 1
for i in range(5):
    for j in range(i + 1):
        print(k, end=' ')
        k = k + 1
    print()