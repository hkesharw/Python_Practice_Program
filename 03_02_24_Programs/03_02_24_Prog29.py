'''

Object :

30.	The current population of a town is 10000. The population of the town is decreasing at the rate of 10% per year. You have to write a program to find out the population at the end of each of the last 10 years. For eg current population is 10000 so the output should be like this:

10th year - 10000
9th year - 9000
8th year - 8100 and so on


'''

population = int(input("Enter the current population : "))
print(f"10th year - 10000")
for i in range(9, 0, -1):
    a = population
    k = a - (population*10)//100
    if i == 1:
        print(f"{i}st year - {k}")
    elif i == 2:
        print(f"{i}nd year - {k}")
    elif i == 3:
        print(f"{i}rd year - {k}")
    else:
        print(f"{i}th year - {k}")
    population = k


