#22.Write a Python program to check whether an element exists within a tuple. 

# Take user input for the tuple
input_string = input("Enter the elements of the tuple separated by spaces:- ")
user_tuple = tuple(map(int, input_string.split()))

# Take user input for the element to find
element_to_find = int(input("Enter the element to search for:- "))

# Check if the element exists in the tuple
if element_to_find in user_tuple:
    print(f"The element {element_to_find} exists in the tuple.")
else:
    print(f"The element {element_to_find} does not exist in the tuple.")
