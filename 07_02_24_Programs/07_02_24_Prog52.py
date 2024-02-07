'''

Object :

53.	Count the frequency of a particular character in a provided string. Eg 'hello how are you' is the string, the frequency of h in this string is 2.

'''

sen = input("Enter the sentence : ")
value = input("Enter the unique which you want to count : ")
count = 0
for i in range(len(sen)):

    if value == sen[i]:
        count = count + 1

print(f"The frequency of {value} in this sentence is {count}")