#36. How Do You Check The Presence Of A Key In A Dictionary?

d1={}
n= int(input("Enter number of pairs:"))
for i in range(n):
    key=input("Enter number of key:")
    Value=input("Enter number of value:")
    d1[key]=Value
print(d1)


key=input("Enter the key you want to check in the dictionary: ")


if 'key' in d1.keys():
    print(f"The key '{key}' the key is present in the dictionary.")
else:
    print(f"The key '{key}' the key is not present in the dictionary.")
