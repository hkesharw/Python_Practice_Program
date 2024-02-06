'''
Object :

12.	Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.
'''

radius = int(input("Enter radius : "))
height = int(input("Enter height : "))

PI = 3.14

volume = PI*radius**2*height
print("Volume is", volume)
cost = volume/100 *40
print("cost is",cost)