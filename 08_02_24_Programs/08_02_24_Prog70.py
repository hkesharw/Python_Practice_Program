'''

Object :

70.	Write a program that can convert a 2D list to 1D list Write a program that can print

'''

two_dimensional_list = [[1, 2, 3], [4, 5, 6]]
one_dimensional_list = []

for i in range(len(two_dimensional_list)):
    for j in range(len(two_dimensional_list[i])):
        one_dimensional_list.append(two_dimensional_list[i][j])

print(two_dimensional_list)
print(one_dimensional_list)

