'''

Object :

69.	Write a program to replace an item with a different item if found in the list

'''

l1 = [2, 3, 5, 6, 2, 7, 2, 8, 9]
item = 2
replace = 'h'

for i in range(len(l1)):
    if l1[i] == item:
        l1[i] = replace

print(l1)


