'''

Object:

65.	Write a program that can count the number of words in a given string

'''

sen = input("Enter the sentence i will tell you the total count of this: ")

count = 0

for i in sen:
    count = count + 1

print(f"Total count of the given sentence is {count}")