'''

Object:

64.	Write a program that can reverse words of a given string (by using string).
Eg - if the input is : Hello how are you
Output should be : you are how Hello
'''

words = input("Enter the sentence : ")

k = words.split(sep=' ')

for i in reversed(k):
    print(i, end=' ')
