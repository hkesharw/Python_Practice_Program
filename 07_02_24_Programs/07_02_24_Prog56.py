'''

Object :

57.	Write a program that can check whether a given string is palindrome or not.

'''

sen = input("Enter the string : ")
temp = sen
k = len(sen)

reverse = sen[::-1]


if temp == reverse:
    print(f"{sen} is palindrome")
else:
    print(f"{sen} is not palindrome")