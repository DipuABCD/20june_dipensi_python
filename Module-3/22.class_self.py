#22. How to Define a Class in Python? What Is Self? Give An Example Of A Python Class.

"""
-> Python classes provide all the standard features of Object Oriented Programming: the class inheritance mechanism allows multiple base classes, 
   a derived class can override any methods of its base class or classes, and a method can call the method of a base class with the same name.
-> As per the syntax above, a class is defined using the class keyword 
-> followed by the class name and : operator after the class name, 
-> which allows you to continue in the next indented line to 
-> define class members. 

-> In object-oriented programming, whenever we define methods for a class, 
-> we use self as the first parameter in each case.
"""

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


student1 = Student("Dipensi", 16, 11)
student2 = Student("Harshvi", 17, 12)


print(student1.get_info())
print(student2.get_info())
