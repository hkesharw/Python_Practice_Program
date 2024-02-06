'''

Object :

33.	User will provide 2 numbers you have to find the by LCM of those 2 numbers

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

lcm = num1*num2//hcf

if lcm<0:
    print(f"The LCM is {-(lcm)} for {num1} and {num2}")
else:
    print(f"The LCM is {(lcm)} for {num1} and {num2}")