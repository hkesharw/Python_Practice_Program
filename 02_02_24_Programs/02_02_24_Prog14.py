'''
Object:

Calculate the angle between the hour hand and minute hand.

Input:
H = 9 , M = 0
Output:
90
Explanation:
The minimum angle between hour and minute
hand when the time is 9 is 90 degress.
'''

hour = int(input("Enter hour:"))
mint = int(input("Enter mint:"))

Angle = 30*hour-(11/2)*mint

if Angle>180:
    Angle = Angle-180
    print("The minimum angle is:", Angle)
elif Angle==180:
    Angle = Angle-180
    print("The minimum angle is:", Angle)
elif Angle<0:
    print(-(Angle))
else:
    print("The minimum angle is:", Angle)
