'''

Object :

43.	Write  a program to print the following pattern
        *
      * * *
    * * * * *
   * * * * * * *
 * * * * * * * * *

'''



for j in range(5):
    for i in range(5 - j):
        print("  ", end='')

    for k in range(1, (j+1)*2):
        print("* ", end='')
    print("")