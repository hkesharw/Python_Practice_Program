'''

Object :

59.	Write a python program to convert a string to title case without using the title()

'''

sen = input("Enter the sentence : ")
y = sen.split(sep=' ')
for i in y:
    print(i.capitalize(),end=' ')