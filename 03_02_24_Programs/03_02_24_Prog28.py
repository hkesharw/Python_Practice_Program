'''

Object :

29.	Print all the armstrong numbers in the range of 100 to 1000

'''

for i in range(100, 10000):

    a = str(i)
    x = int(a)
    k = len(a)
    j = 0
    for i in range(k):
        m = int(a[i])
        j = j + m ** k

    if x == j:
        print(f"Armstrong number: {x}")





