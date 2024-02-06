'''

Object:

32.	User will provide 2 numbers you have to find the HCF of those 2 numbers

'''

num1 = int(input("enter the number : "))
num2 = int(input("enter the number : "))

if num1<num2:
    mn = num1
else:
    mn = num2
hcf = 1
for i in range(2,mn+1):
    if num1%i ==0 and num2%i==0:
        hcf = i

print(hcf)