#29. What relationship is appropriate for Student and Person?

"""
-> association.
-> In the context of an educational institution, the relationship between "Student" and "Person" can be described as a subset of the broader 
   relationship between "Person" and "Individual." Here's how the relationships work:-
   (1) Inheritance Relationship (Person and Individual):- In a broader sense, "Person" is a superclass or parent class that encompasses all 
       individuals, regardless of whether they are students or not. 
   (2) Specific Relationship (Student and Person): A "Student" is a specific type of "Person" who is currently engaged in an educational 
       program at an institution.
-> To put it simply, "Person" is the overarching category that includes all individuals, while "Student" is a more specific category that 
   falls under "Person," indicating individuals who are pursuing education within an institution.
-> In terms of database design or object-oriented programming,  this relationship could be implemented using inheritance, where a "Student" 
   class inherits properties and methods from a "Person" class. 

"""