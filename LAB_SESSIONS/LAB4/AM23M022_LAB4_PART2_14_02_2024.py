# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 22:18:22 2024

@author: mdine
"""
'''

6. Store the employee IDs, names, salaries, and years of experience using nested dictionaries (the key of the highest level dictionary can be the employee ID). 

a) Sort this dictionary using the salary value. 

b) Add a new employee to the dictionary in the correct position (sorted as mentioned above).
''' 

employees = {
    101: {'name': 'Dinesh', 'salary': 80000, 'experience': 3},
    102: {'name': 'Shubhangi', 'salary': 100000, 'experience': 3},
    103: {'name': 'Kavi', 'salary': 75000, 'experience': 2}
}

sort= dict(sorted(employees.items(), key=lambda item: item[1]['salary']))



for emp_id, emp_info in sort.items():
    print(f"{emp_id},{emp_info['name']}, {emp_info['salary']},{emp_info['experience']}")

new_employee = {'name': 'Kirthika', 'salary': 95000, 'experience': 4}
employees[104] = new_employee

print(employees)

sort= dict(sorted(employees.items(), key=lambda item: item[1]['salary']))

for iid , info in sort.items():
    print(iid, info['name'],info['salary'], info['experience'])
    
'''    
7. You are given two Python dictionaries, A and B, 
with keys as alphabets and values as random integers. 
Write a Python function to create a third dictionary C, 
that combines A and B. For common keys, 
the value in C should be the sum of values from A and B.
'''


# Example dictionaries A and B
dictA = {'a': 1, 'b': 2, 'c': 3}
dictB = {'b': 5, 'c': 7, 'd': 9}

# Create a third dictionary C by combining A and B
dictC = {}

# Combine values from A and B for common keys
for key in dictA:
    if key in dictB:
        dictC[key] = dictA[key] + dictB[key]
    else:
        dictC[key] = dictA[key]

# Add keys from B not present in A
for key in dictB:
    if key not in dictA:
        dictC[key] = dictB[key]

print(dictC)

'''
 8. Assume you have a list of lists, where each inner list contains two elements:
    a key and a value. Write a Python function that takes the list of lists as input and returns a list of dictionaries, 
    where each dictionary contains a key-value pair from the original input list.
'''

def list_to_dict(list_of_lists):
    dictionary = []
    for inner_list in list_of_lists:
        dictionary.append({inner_list[0]: inner_list[1]})
    return dictionary

lst = [['Dk', 'programming'], ['kd', 'machine learning'], ['ds', 'data analysis']]
output = list_to_dict(lst)
print(output)


'''
9. Illustrate the usage of positional and keyword arguments using suitable examples.
'''
def greet(name, greeting):
    return (f"{greeting}, {name}!")

# Using positional arguments
print(greet("Dinesh", "Hello"))  
# Using keyword arguments
print(greet(greeting="Hi", name="Bob")) 

'''
10. Write a function to find the maximum of n numbers 
using variable length positional arguments
'''

def maximum_nnos(*arg):
    if len(arg)==0:
        return "No input provided"
    else:
        return max(arg)
input=(4,55,62,456)
print(maximum_nnos(*input))

'''
11. Write a function to concatenate n strings 
using variable length keyword arguments.
'''

def concatenate_strings(**kwargs):
    concatenated_string = ""
    for key, value in kwargs.items():
        concatenated_string += value
    return concatenated_string

print(concatenate_strings(s1="Hello", s2=" ", s3="world", str4="!")) 




