'''

Object :

71.	Write a program that can perform union and intersection on 2 given list.

'''

l1 = [2, 3, 5, 6]
l2 = [2, 3, 4, 2]
k = list(l2)


for i in range(len(l1)):

    item = l1[i]

    for j in range(len(k)-1):

        if k[j] == item:

            k.remove(k[j])
print(f"first list {l1}")
print(f"Second list {l2}")

print(f"Intersecion of first and second list {l1+k}")
print(f"Union of first and second list {l1+l2}")

