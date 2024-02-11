'''

Object :

72.	Print the max item of each row of a matrix.

'''

rows = int(input("Enter how many rows you want in matrix : "))
cols = int(input("Enter how many cols you want in matrix : "))
y = 0
l1 = []
mx = []
for i in range(rows):
    l2 = []
    for j in range(cols):
        k = []
        l2.append(int(input("Enter the element : ")))
    k = l2
    mx.append(max(k))
    del k
    l1.append(l2)

print(l1)
print(f"max items each row {mx}")
