#61. Write a Python program to calculate the area of a parallelograme.

# Input the base and height of the parallelogram
base = float(input("Enter the base length of the parallelogram:- "))
height = float(input("Enter the height of the parallelogram:- "))

# Check if the base and height are positive numbers
if base < 0 or height < 0:
    print("Base and height should be positive numbers.")
else:
    # Calculate the area of the parallelogram
    area = base * height
    print(f"The area of the parallelogram is: {area}")
