'''

Object :

67.	Create 2 lists from a given list where 1st list will contain all the odd numbers from the original list and the 2nd one will contain all the even numbers

'''

l1 = [2, 5, 4, 7, 8, 10, 11, 14, 13, 98, 1023, 7865432, 432, 20, 87]

l2 = []
l3 = []

for i in l1:
    if i % 2 == 0:
        l2.append(i)
    else:
        l3.append(i)

print(f"Given list are {l1}")
print(f"Even number new list are {l2}")
print(f"Odd number new list are {l3}")
