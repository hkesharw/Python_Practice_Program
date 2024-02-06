'''
Object :

11.	Write a program to find the simple interest when the value of principle,rate of interest and time period is given.
'''

principle = int(input("Enter principle: "))
rate = int(input("Enter rate : "))
t = int(input("enter time : "))

si = (principle*rate*t)/100

print("Total Interst is:", si)