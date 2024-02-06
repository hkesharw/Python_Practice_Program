'''
Object:

22.	Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
'''

def calculate_animals(heads, legs):
    # Assuming each dog has 4 legs and each chicken has 2 legs
    dog_legs = 4
    chicken_legs = 2

    # Calculate the number of dogs using the system of equations
    # 1. Number of dogs + Number of chickens = Total heads
    # 2. Number of dog legs + Number of chicken legs = Total legs

    # Solving the equations to find the number of dogs
    num_dogs = (legs - (chicken_legs * heads)) / (dog_legs - chicken_legs)

    # Calculate the number of chickens based on the number of dogs
    num_chickens = heads - num_dogs

    # Check if the calculated values are valid (non-negative integers)
    if num_dogs >= 0 and num_chickens >= 0 and num_dogs.is_integer() and num_chickens.is_integer():
        return int(num_dogs), int(num_chickens)
    else:
        return None

# Get user input for total heads and legs
total_heads = int(input("Enter the total number of heads: "))
total_legs = int(input("Enter the total number of legs: "))

# Calculate the number of dogs and chickens
result = calculate_animals(total_heads, total_legs)

# Display the result
if result:
    num_dogs, num_chickens = result
    print(f"There are {num_dogs} dogs and {num_chickens} chickens.")
else:
    print("Invalid input. Unable to determine the number of dogs and chickens.")


