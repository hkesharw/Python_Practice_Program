'''
Object:

Given two rectangles, find if the given two rectangles overlap or not. A rectangle is denoted by providing the x and y coordinates of two points: the left top corner and the right bottom corner of the rectangle. Two rectangles sharing a side are considered overlapping. (L1 and R1 are the extreme points of the first rectangle and L2 and R2 are the extreme points of the second rectangle).

Input:
L1=(0,10)
R1=(10,0)
L2=(5,5)
R2=(15,0)
Output:
1
Explanation:
The rectangles overlap.

Input:
L1=(0,2)
R1=(1,1)
L2=(-2,0)
R2=(0,-3)
Output:
0
Explanation:
The rectangles do not overlap.

'''

x1 = int(input("Enter x1 value: "))
x2 = int(input("Enter x2 value: "))
x3 = int(input("Enter x3 value: "))
x4 = int(input("Enter x4 value: "))
y1 = int(input("Enter y1 value: "))
y2 = int(input("Enter y2 value: "))
y3 = int(input("Enter y3 value: "))
y4 = int(input("Enter y4 value: "))

if (x2 > x3 and x1 < x4) and (y2 > y3 and y1 < y4):
    print("The rectangles overlap")
else:
    print("The rectangle do not overlap")
