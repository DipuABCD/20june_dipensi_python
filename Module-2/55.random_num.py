# 55. How can you get a random number in python? 

"""import random

y="y"
while y!="n":
    t=random.randint(11111,99999)
    print(t)
    y=input("Do you want to countinue 'y' for 'yes' 'n' for 'no' :-")"""

import random

while True:
    lower_bound_str = input("Enter the lower bound of the range: ")
    upper_bound_str = input("Enter the upper bound of the range: ")

    if not (lower_bound_str.isdigit() and upper_bound_str.isdigit()):
        print("Invalid input. Please enter valid integer values.")
    else:
        lower_bound = int(lower_bound_str)
        upper_bound = int(upper_bound_str)

        if lower_bound >= upper_bound:
            print("Lower bound should be less than upper bound.")
        else:
            # Generate a random integer within the specified range
            random_number = random.randint(lower_bound, upper_bound)
            print("Random number:", random_number)

            # Ask the user if they want to generate another random number
            choice = input("Do you want to generate another random number? (yes/no): ")
            if choice.lower() != 'yes':
                break
