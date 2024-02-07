'''

Object :

59.	Write a python program to convert a string to title case without using the title()

'''

sen = input("Enter the sentence : ")
updated_sen = sen.replace(sen[0],sen[0].capitalize())
print(updated_sen)
count = 0
for i in updated_sen:
    if i == ' ':
        k = updated_sen[count+1].capitalize()
        print(k,end='')
        updated_sen.replace(k, '')
    else:
        print(i, end='')
        count = count + 1
        print(count)