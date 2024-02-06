'''

Object :

31.	Write a program to print all the unique combinations of 1,2,3 and 4


'''

num1 = int(input("Enter the number "))
num2 = int(input("Enter the number "))
num3 = int(input("Enter the number "))
num4 = int(input("Enter the number "))

for i in range(5):
    for j in range(5):
        for k in range(5):
            for l in range(5):
                if i!=j and j!=k and k!=l and l!=i:
                    print(i,j,k,l)