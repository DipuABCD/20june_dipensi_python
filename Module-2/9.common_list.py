#9. Write a Python function that takes two lists and returns true if they have at least one common member.

input_list1=input("Enter elements of the first list separated by spaces:- ")
list1 =set(input_list1.split())

input_list2=input("Enter elements of the second list separated by spaces:- ")
list2 =set(input_list1.split())

result = bool(list1.intersection(list2))
print("Result:-",result)