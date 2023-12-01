#60. Write a Python program to calculate the area of a trapezoid.

# Input from the user
base1 = float(input("Enter the length of the first base:- "))
base2 = float(input("Enter the length of the second base:- "))
height = float(input("Enter the height:- "))

# Check if the values are valid (non-negative)
if base1 < 0 or base2 < 0 or height < 0:
    print("Base and height values must be non-negative.")
else:
    # Calculate the area of the trapezoid using the formula
    area = 0.5 * (base1 + base2) * height

    print("The area of the trapezoid is:", area)
