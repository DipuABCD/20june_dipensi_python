#5.How will you compare two lists?
"""
-> To check whether two lists contain the same elements or not, we can use the sort() method to sort the elements 
of the lists first. Then, we can compare the two lists. For comparison,first we will check if the length of the 
lists are equal or not. If the lengths are not equal, the lists will be automatically considered as different.
-> When programming in, or learning, Python you might need to determine whether two or more lists are equal. When you
compare lists for equality, you were checking whether the lists are the same length and whether each item in the list 
is equal. Lists of different lengths are never equal."""

l1 = [10, 20, 30, 40, 50] 
l2 = [20, 30, 60, 40, 70] 

l1.sort() 
l2.sort() 


if l1 == l2: 
    print ("The lists l1 and l2 are the same") 
else: 
    print ("The lists l1 and l2 are not the same") 

