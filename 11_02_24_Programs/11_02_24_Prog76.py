'''

Object :

77.	Write a program that can sort a given unsorted list. Dont use any built in function for sorting.

'''

l1 = [5, 20, 87, 9, 1]

print(l1)
print(len(l1))

for i in range(len(l1)):

    for j in range(0, len(l1)-i-1):

        if l1[j] >= l1[j+1]:
            l1[j], l1[j+1] = l1[j+1], l1[j]

print(l1)
