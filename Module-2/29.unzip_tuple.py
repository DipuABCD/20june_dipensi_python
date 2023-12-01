#29. Write a Python program to unzip a list of tuples into individual lists.

# Get user input for the list of tuples
list_of_tuples = []
while True:
    try:
        num = int(input("Enter the first element of the tuple (or any non-integer to stop): "))
        value = input("Enter the second element of the tuple: ")
        tuple_item = (num, value)
        list_of_tuples.append(tuple_item)
    except ValueError:
        break

# Unzip the list of tuples into separate lists using list comprehension and map function
unzipped_lists = [list(x) for x in zip(*list_of_tuples)]

print("Original list of tuples:")
print(list_of_tuples)

print("Unzipped lists:")
for index, individual_list in enumerate(unzipped_lists):
    print(f"List {index + 1}: {individual_list}")
