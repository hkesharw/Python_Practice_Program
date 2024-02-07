'''

Object :

55.	Count the number of vowels in a string provided by the user.

'''

sen = input("Enter the sentence so that i will tell you how many vowels you have used : ")
count = 0
for i in range(len(sen)):
    if sen[i] == 'a' or sen[i] == 'e' or sen[i] == 'i' or sen[i] == 'o' or sen[i] == 'u':
        count = count + 1

print(f"Total number of vowels in this - {sen} : is {count}")
