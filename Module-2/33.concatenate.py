#33. Write a Python script to concatenate following dictionaries to create a new one.

# Get user input for three dictionaries
dict1 = {input("Enter key {}: ".format(i + 1)): 
        input("Enter value for key {}: ".format(i + 1)) 
         for i in range(int(input("Enter the number of key-value pairs in the first dictionary: ")))}

dict2 = {input("Enter key {}: ".format(i + 1)): 
        input("Enter value for key {}: ".format(i + 1)) 
         for i in range(int(input("Enter the number of key-value pairs in the second dictionary: ")))}

dict3 = {input("Enter key {}: ".format(i + 1)): 
        input("Enter value for key {}: ".format(i + 1)) 
         for i in range(int(input("Enter the number of key-value pairs in the third dictionary: ")))}

# Concatenate dictionaries
concatenated_dict = {**dict1, **dict2, **dict3}

# Display the concatenated dictionary
print("\nConcatenated Dictionary:", concatenated_dict)
