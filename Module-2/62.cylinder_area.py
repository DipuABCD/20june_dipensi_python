#62. Write a Python program to calculate surface volume and area of a cylinde.

# Get user input for radius and height using list comprehension
radius, height = [float(input(f"Enter the {param} of the cylinder: ")) for param in ["radius", "height"]]

# Calculate surface area and volume
pi = 3.14159  # Approximate value of pi
surface_area = 2 * pi * radius * (radius + height)
volume = pi * radius ** 2 * height

# Display results
print("Radius of the cylinder:", radius)
print("Height of the cylinder:", height)
print("Surface Area of the cylinder:", surface_area)
print("Volume of the cylinder:", volume)
