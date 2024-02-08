'''

Object :

71.	Write a program that can perform union and intersection on 2 given list.

'''

l1 = [2, 3, 5, 6]
l2 = [2, 3, 4, 2]
l3 = []
for i in range(len(l1)):
    item = l1[i]
    k = len(l2)
    for j in range(k):
        if item == l2[j]:
            l2.pop()
    l3.append(l1[i])

l3.append(l2)

print(l1)
print(l2)
print(l3)




