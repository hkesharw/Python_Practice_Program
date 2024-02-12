'''

Object :

75.	Write a program that can check if you can perform matrix multiplication on 2 matrices

'''


def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)
    return matrix

def multiply_matrices(matrix1, matrix2):
    result_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = 0
            for k in range(len(matrix2)):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result_matrix.append(row)
    return result_matrix

# Example: Taking two matrices as input and multiplying them
rows1 = int(input("Enter the number of rows for matrix 1: "))
cols1 = int(input("Enter the number of columns for matrix 1: "))
matrix1 = input_matrix(rows1, cols1)

rows2 = int(input("Enter the number of rows for matrix 2: "))
cols2 = int(input("Enter the number of columns for matrix 2: "))
matrix2 = input_matrix(rows2, cols2)

# Check if the matrices can be multiplied
if cols1 != rows2:
    print("Error: Matrices cannot be multiplied.")
else:
    result = multiply_matrices(matrix1, matrix2)
    print(result)
    # Displaying the result matrix
    print("\nResulting Matrix after multiplication:")
    for i in range(len(result)):
        for j in range(len(result[0])):
            print(result[i][j], end=" ")
        print()
