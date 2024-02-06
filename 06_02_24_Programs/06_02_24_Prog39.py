'''

Object :

40.	Find the reverse of a number provided by the user(any number of digit)


String slicing concept :


arr[start:stop]         # items start through stop-1
arr[start:]             # items start through the rest of the array
arr[:stop]              # items from the beginning through stop-1
arr[:]                  # a copy of the whole array
arr[start:stop:step]    # start through not past stop, by step

source - GeeksForGeeks

for more better understanding prefer ChatGpt

'''

num = input("Enter the number : ")

print(num[::-1])