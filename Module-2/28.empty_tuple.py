#28. Write a Python program to remove an empty tuple(s) from a list of tuples.

# Get user input for the list of tuples
num_tuples = int(input("Enter the number of tuples:- "))
list_of_tuples = [tuple(map(int, input(f"Enter tuple {i + 1} (comma-separated values): ").split(','))) 
                  for i in range(num_tuples)]

# Removing empty tuples using list comprehension
cleaned_list = [tup for tup in list_of_tuples if tup]

print("Original list of tuples:", list_of_tuples)
print("List of tuples after removing empty tuples:", cleaned_list)
