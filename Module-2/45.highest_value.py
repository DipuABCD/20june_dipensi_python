#45 Write a Python program to find the highest 3 values in a dictionary.

# User input to create the dictionary
my_dictionary = {}
num_entries = int(input("Enter the number of dictionary entries:- "))

for i in range(num_entries):
    key = input(f"Enter key {i + 1}:- ")
    value = int(input(f"Enter value for key {i + 1}:- "))
    my_dictionary[key] = value

# Get the values from the dictionary and sort them in descending order
values_sorted = sorted(my_dictionary.values(), reverse=True)

# Get the highest 3 values
highest_3_values = values_sorted[:3]
print("Highest 3 values:-", highest_3_values)

