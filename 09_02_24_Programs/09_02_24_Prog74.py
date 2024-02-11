'''

Object :

74.	Write a program to print the shape of a matrix.

'''

row = int(input("Enter the rows : "))
col = int(input("Enter the cols : "))

matrix = []

for i in range(row):
    rows = []
    for j in range(col):
        k = int(input("Enter the element : "))
        rows.append(k)
    matrix.append(rows)

print(matrix)
j = 0
l = 0
for l in matrix:
    j = j + 1
print(f"The shape of matrix is {j} * {len(l)}")

