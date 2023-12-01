#31.  How will you create a dictionary using tuples in python?

n = int(input("Enter the number of tuples you want to enter: "))
tuple={}
for i in range(n):
    key1=int(input(f"Enter the first element of tuple {i + 1}: "))
    key2=int(input(f"Enter the second element of tuple {i + 1}: "))
    value=(input(f"Enter the corresponding value for tuple {i + 1}: "))
    tuple[(key1,key2)] = value

print("The resulting dictionary is:")
print(tuple)
