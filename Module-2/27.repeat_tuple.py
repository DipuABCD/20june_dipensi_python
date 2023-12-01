#27.  Write a Python program to find the repeated items of a tuple.
# User input for tuple elements
input_str = input("Enter elements of the tuple separated by spaces:- ")
elements = input_str.split()

# Check if all elements are valid integers
if all(item.isdigit() for item in elements):
    tuple_data = tuple(map(int, elements))
    
    # Count occurrences of elements using a dictionary
    element_counts = {}
    for item in tuple_data:
        element_counts[item] = element_counts.get(item, 0) + 1
    
    # Find repeated items
    repeated_items = [item for item, count in element_counts.items() if count > 1]
    
    if repeated_items:
        print("Repeated items:", repeated_items)
    else:
        print("No repeated items found.")
else:
    print("Invalid input. Please enter valid integers separated by spaces.")
