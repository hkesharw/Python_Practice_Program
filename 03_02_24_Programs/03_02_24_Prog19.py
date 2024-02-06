'''
Object:

20.	Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%), and tax(if salary is between 5-10 lakh–10%),(11-20lakh–20%),(20<– 30%)(0-1lakh print k).
'''

gross_salary = float(input("Enter your gross salary : "))

hra = gross_salary*10/100
print("hra:",hra)
da = gross_salary*5/100
print("da:",da)
pf = gross_salary*3/100
print("pf:",pf)

if gross_salary>=500000 and gross_salary<=1000000:
    tax = gross_salary*10/100
    print("Tax:",tax)
    inhand_salary = gross_salary - hra - da - pf - tax
    print("Your Inhand Salary is :", inhand_salary)
elif gross_salary>1000000 and gross_salary<=2000000:
    tax = gross_salary*20/100
    print("Tax:", tax)
    inhand_salary = gross_salary - hra - da - pf - tax
    print("Your Inhand Salary is :", inhand_salary)
elif gross_salary>2000000 and gross_salary<=3000000:
    tax = gross_salary*30/100
    inhand_salary = gross_salary - hra - da - pf - tax
    print("Tax:", tax)
    print("Your Inhand Salary is :", inhand_salary)
else:
    inhand_salary = gross_salary - hra - da - pf
    print("Your Inhand Salary is :", inhand_salary)

