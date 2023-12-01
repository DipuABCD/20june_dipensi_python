#4. Write a Python function to get the largest number, smallest num and sum of all from a list.

NumList = []
Number = int(input("Please enter the Total Number of List Elements:- "))
for i in range(Number):
    value = int(input("Please enter number :- " ))
    NumList.append(value)

print("The largest Number in this List is :- ", min(NumList))
print("The smallest Number in this List is :- ", max(NumList))
print("Sum of all list number :-",sum(NumList))
