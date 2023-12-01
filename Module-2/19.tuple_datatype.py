#19. Write a Python program to create a tuple with different data types.
def different_data_type():
    element1 = int(input("Enter an integer number:- "))
    element2 = input("Enter a string:- ")
    element3 = float(input("Enter a float:- "))
    element4 = bool(input("Enter a boolen (true/false):- "))
    element5 = input("Enter a list (comma- separated elements):- ").split(',')
    element6_name = input("Enter a dictionary key (name):- ") 
    element6_age = input("Enter a dictionary value (age):- ")
    element6 = {element6_name: element6_age}

    data_type = (element1,element2,element3,element4,element5,element6)
    return data_type
result_tuple = different_data_type()
print(result_tuple)