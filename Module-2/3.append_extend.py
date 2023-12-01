#3. Differentiate between append () and extend () methods? 

"""
->  append : it is use to add single element in the end of the list. Add an item to the end of the list. 
->  extend : it is use to add a list in the end of the another list. 
"""
#append example:
tech=['java','python','php','ruby','react','angular']
print(tech)
tech.append('c++')
print(tech)

#extend example:
tech=['java','python','php','ruby','react','angular']
newtech=["c","c++","css","js"]
print(newtech)
tech.extend(newtech)
print(tech)