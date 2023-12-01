#11. Write a Python function that takes a list and returns a new list with unique 
#elements of the first list.

def get_uni_element():
    input_list = input("Enter the elements of the list separated by spaces:- ").split()
    unique_element = []

    for element in input_list:
        if element not in unique_element:
            unique_element.append(element)
    return unique_element

unique_list = get_uni_element()
print(unique_list)