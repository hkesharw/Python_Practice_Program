'''

Object :

41.	Write a program to print the following pattern
*
**
***
****
*****

'''

for i in range(5):
    for j in range(i+1):
        print("*", end= ' ')
    print()
