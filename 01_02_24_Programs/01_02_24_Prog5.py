'''
Object - 5.	Write a program that will reverse a four digit number.Also it checks whether the reverse is true
'''

number = int(input("enter the four digit number : "))
reverse_number = int(input("enter the reverse number : "))

temp = number

temp = temp%10
k = temp*1000
number = number//10
temp = number
temp = temp%10
k = k + temp*100
number = number//10
temp = number
temp = temp%10
k = k + temp*10
number = number//10
k = k+number
print(k)

if k == reverse_number:
    print("Checked and Matched")
else:
    print("Checked but not matched")