'''

Object :

62.	Write a python program to search a given number from a list

'''

l1 = []
n = 5

for i in range(n):
    l1.append(input("Enter the elements you want to add in the list :"))

value = input("Enter the value you want to search : ")
count = 1
for i in l1:
    if i == value:
        print(f"The value you are searching for '{value}' is exist at this position {count}")
    else:
        count = count + 1