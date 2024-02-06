'''
Object -
10.	Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit
'''
cp = int(input("Enter Cost Price: "))
sp = int(input("Enter Selling Price : "))

if sp>cp:
    print("Profit")
else:
    print("Loss")