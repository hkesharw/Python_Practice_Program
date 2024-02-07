'''

Object :

Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the numbers.

'''
import sys
result = 0
count = 0

while True:
    n = int(input("Enter the number : "))
    if n == 0:
        print(f"The total sum of the given number by user is {result}")
        avg = result/count
        print(f"The total average of the given number by user is {avg}")
        sys.exit()
    else:
        result = result + n
        count = count + 1






