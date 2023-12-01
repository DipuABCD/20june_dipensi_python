#30. Write a Python program to convert a list of tuples into a dictionary. 

# Get the number of tuples from user input
num_tuples = int(input("Enter the number of tuples: "))

# Initialize an empty dictionary and get key-value pairs for each tuple from user input
converted_dict = {input("Enter the key: "): input("Enter the value: ") for _ in range(num_tuples)}

# Display the resulting dictionary
print("Converted dictionary:")
print(converted_dict)
