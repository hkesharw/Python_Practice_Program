'''
Object:

21.	Write a menu driven program -
1.cm to ft
2.kl to miles
3.usd to inr
4.exit
'''
import sys

option = input("Choose the options "
               "1.cm to ft"
               " 2.kl to miles"
               " 3.usd to inr"
               " 4.exit: ")

k = int(option)

while(True):
    if k==1:
        cm = float(input("enter cm: "))
        ft = cm/30.48
        print("cm to ft is:",ft)
    elif k==2:
        kl = float(input("enter kl: "))
        miles = kl*0.621371
        print("KL to Miles is:",miles)
    elif k==3:
        usd = float(input("Enter usd : "))
        inr = usd*83
        print("USD to INR is:",inr)
    elif k==4:
        sys.exit()

    rerun = input("Do you want to run the program again(Y/N) : ")
    if rerun == 'Y' or rerun == 'y':
        option = input("Choose the options "
                       "1.cm to ft"
                       " 2.kl to miles"
                       " 3.usd to inr"
                       " 4.exit: ")

        k = int(option)
    else:
        sys.exit()







