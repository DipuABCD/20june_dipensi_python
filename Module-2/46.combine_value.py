#46.Write a Python program to combine values in python list of dictionaries. Sample data: [{'item': 'item1', 
#'amount': 400}, {'item': 'item2', 'amount': 300}, o {'item': 'item1', 'amount': 750}] 
#Expected Output:Counter ({'item1': 1150, 'item2': 300})

sample_data = []
num_items = int(input("Enter the number of items:- "))

for i in range(num_items):
    item = input(f"Enter the name of item {i+1}:- ")
    amount = int(input(f"Enter the amount for item {i+1}:- "))
    sample_data.append({'item': item, 'amount': amount})

combined_values = {}
for d in sample_data:
    item = d['item']
    amount = d['amount']
    combined_values[item] = combined_values.get(item, 0) + amount

print("combined_values:",combined_values)

