'''

Object :

42.	Write a program to print the following pattern

*
**
***
**
*

'''

for i in range(5):
    if i >= 3:
        for j in range(5 - i):
            print("*", end='')
    else:
        for j in range(i+1):
            print("*", end='')
    print()