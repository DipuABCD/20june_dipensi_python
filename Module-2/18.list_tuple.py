#18. What is tuple? Difference between list and tuple.

""" 
->Tuple is a collection which is ordered and unchageable.
->Allows duplicate members.
->The differences between tuples and lists are, the tuples cannot bechanged unlike lists and tuples use parentheses,
 whereas lists use square brackets.
->list has variable length, tuple has fixed length.
->list has mutable nature, tuple has immutable nature.
->list has more functionality than the tuple.
"""

#tuple example:
tup=[]
n=int(input("Enter Number Of Value:-"))
for i in range(n):
    x=input("Enter A Value:-")
    tup.append(x)

print(tuple(tup))

#list example:
tech=[]
n=int(input("Enter Number Of Element:-"))

for i in range(n):
    x=input("Enter Your Name:-")
    tech.append(x)

tech.sort()
print(tech)