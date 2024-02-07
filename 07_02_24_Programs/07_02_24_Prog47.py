'''

Object :

48.	The natural logarithm can be approximated by the following series.

x-1/x + 1/2((x-1)/x))**2 + 1/2((x-1)/x))**3 + 1/2((x-1)/x))**4 + 1/2((x-1)/x))**5 + ..... + 1/2((x-1)/x))**n
'''

num = int(input("Enter the number : "))
loop = int(input("Enter the number of times you want to count this series : "))

k = (num-1)/num
result = 0
for i in range(1, loop):

    result = result + 1/2*(k**(i+1))

total = k + result

print(f"The Total count of this series is {total}")

