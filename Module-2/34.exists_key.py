#34. Write a Python script to check if a given key already exists in a dictionary.

# Take user input for the dictionary (assuming the input is in the format: key1:value1 key2:value2 ...)
user_input = input("Enter the dictionary (key-value pairs separated by spaces): ")
input_dict = dict(pair.split(":") for pair in user_input.split())

# Take user input for the key to check
key_to_check = input("Enter the key to check: ")

if key_to_check in input_dict:
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")
