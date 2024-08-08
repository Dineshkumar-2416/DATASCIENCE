# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 10:07:22 2024

@author: mdine
"""
# SET OPERATIONS
setA = {10, 20, 30, 40, 40, 50}
setB = {30, 40, 50, 60, 70}
print('Union of two sets : ', setA | setB)
print('Intersection of two sets : ', setA & setB)
print('A - B : ', setA - setB)
print('B - A : ', setB - setA)
print('Symmetry difference of two sets : ', setA ^ setB)

setC = setA - setB
setD = setB - setA
print('Symmetry difference of two sets : ', setC | setD)
setA -= setB
print(setA)



A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A |= B
print("A after A |= B:", A)

A = {1, 2, 3, 4}
A &= B
print("A after A &= B:", A)

A = {1, 2, 3, 4}
A -= B
print("A after A -= B:", A)

B = {3, 4, 5, 6}
B -= A
print("B after B -= A:", B)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
A ^= B
print("A after A ^= B:", A)

# Dictionaries
'''
Dictionary is a collection of key-value pair rep. as key : value
'''
# dct1 = {10 : 100, 20 : 200, ‘ED1’ : ‘name1’, ‘ED2’ : ‘name2’}
# dct1 - identifier
dct1 = {20 : 100, 10 : 200, 'ED2' : 'name1', 'ED1' : 'name2'} 

print('Printing the entire dictionary : ', dct1)

print('Printing using the key values ; ', dct1[10], dct1['ED1'])


print('Using Iterator over key-value pairs');
for k, v in dct1.items(): 
    print(k, v)
    
#.items() - MEMBER FUNCTION


# print('Iterate over keys: prints only keys');
# for k in dct1.keys():
#     print(k)

for k in dct1:
    print(k)
    
# .key()
# .items()  -- MEMBER FUNCTION

# sorted() - built in  function

dct2 = {88:'k', 96:'l',3:'m'}
sorted(dct2)
print(dict(sorted(dct2)))

my_dict = {'b': 3, 'a': 1, 'c': 2}
print(my_dict.items())

sorted_dict_keys = dict(sorted(my_dict.items()))
print(sorted_dict_keys)

'''
Sorting by Values:
You can also sort a dictionary based on its values. This can be done by using the sorted() function along with a lambda function as the key argument and specifying key=lambda x: x[1], where x[1] refers to the values
'''

my_dict = {'a': 1, 'b': 2}


my_dict['a'] = 10

print(my_dict)

my_dict = {'a': 1, 'b': 2, 'c': 3}


del my_dict['b']

print(my_dict)


my_dict.pop('c')

print(my_dict)
'''Two dictionaries cannot be concatenated using + (instead, use update( )).

'''
new = dict()
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
new.update(dict1)
new.update(dict2)
print(new)
dict1.update(dict2)
print(dict1)

# HW: Define a dictionary of student names and find the max, min of the 
# dictionary. Arrange them in sorted order. Print all of them clearly. Also 
# perform addition, deletion and modification of a few of the entries. 
# What are you observations on max, min and sorting?

'''
 Define three dictionaries and concatenate all 
of them in another dictionary. Clear the contents 
of all of them. Check if the dictionaries are empty
'''

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

concatenated_dict = {}
concatenated_dict.update(dict1)
concatenated_dict.update(dict2)
concatenated_dict.update(dict3)

print(concatenated_dict)

dict1.clear()
dict2.clear()
dict3.clear()
print(dict1)
print(dict2)
print(dict3)

print(not bool(dict1))
print(not bool(dict2))
print(not bool(dict3))




    
    