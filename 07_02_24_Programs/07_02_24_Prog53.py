'''

Object :

54.	Find the index position of a particular character in another string.

'''
sen = input("Enter the sentence : ")
value = input("Enter the character to get the index position of that : ")
count = []
for i in range(len(sen)):
    if value == sen[i]:
        count.append(i)

print(f"The index position of {value} is {count}")