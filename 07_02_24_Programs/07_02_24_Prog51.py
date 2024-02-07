'''

Object :

52.	Extract username from a given email.
Eg if the email is nitish24singh@gmail.com then the username should be nitish24singh

'''
import sys

email = input("Enter email : ")

k = len(email)

for i in range(k):
    if email[i] == '@':
        email.replace('@', '')
        sys.exit()
    else:
        print(email[i], end='')

