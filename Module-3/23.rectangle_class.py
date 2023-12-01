#23. Write a Python class named Rectangle constructed by a length and 
#    width and a method which will compute the area of a rectangle 

class Rectangle:
    def rectangle(self, length, width):
        self.length = length
        self.width = width
    
    def compute_area(self):
        return self.length * self.width


user_length = float(input("Enter the length of the rectangle:- "))
user_width = float(input("Enter the width of the rectangle:- "))


user_rectangle = Rectangle(user_length, user_width)


area = user_rectangle.compute_area()
print(f"The area of the rectangle is:- {area}")
