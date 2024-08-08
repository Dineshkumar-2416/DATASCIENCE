# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 17:15:31 2024

@author: mdine
"""
# 10.  Create a set of all numbers between 1 and 20 that are either divisible by 3 or 5, using set comprehension.
# Set comprehension to generate a set of numbers between 1 and 20 that are divisible by 3 or 5
result_set = {num for num in range(1, 21) if num % 3 == 0 or num % 5 == 0}

# Print the resulting set
print(result_set)

'''
List comprehension  : Given two lists of equal length, list1 contains the integers and list2 contains alphabets. Using list comprehension, WAP

a) To generate a list containing the squares of elements from list1.

b) To generate a list containing pairwise corresponding elements in the form of tuple.

c) To generate a list containing all possible combinations of elements from the two lists.

d) To generate a list containing elements of list1 and list2 alternatively
'''
list1 = [3,4]
list2 = ['d','k']
# a) To generate a list containing the squares of elements from list1.
sqr = [i**2 for i in list1]
print(sqr)
# To generate a list containing pairwise corresponding elements in the form of tuple

pair = [(x,y) for x,y in zip(list1 , list2 )]
print(pair)

# c) To generate a list containing all possible combinations of elements from the two lists.
list1 = [3,4]
list2 = ['d','k']
pos = [(x,y) for  x in list1 for y in list2 ]
print(pos)

# d) To generate a list containing elements of list1 and list2 alternatively
list1 = [3,4]
list2 = ['d','k']
alt = [elem for l in zip(list1 , list2 ) for elem in l]
print(alt)

'''
8. Write a code snippet in Python that takes a string as input and returns a tuple of tuples. Each inner tuple should contain a character from the input string and its corresponding ASCII value.

Sample example: Input_string = "Design",  Output_tuple = (('D', 68), ('e', 101), ('s', 115), ('i', 105), ('g', 103),('n', 110) )

'''
input_str = "Dinesh"
ascii_value =[]
for i in input_str:
    ascii_value.append((i ,ord(i)))
    
print(tuple(ascii_value))
'''
9. Create a program that takes a list of tuples containing student name and roll number and returns a new list of tuples containing only those tuples whose first element is a vowel (a, e, i, o, u, A, E, I, O, U).

Sample example: list_of_tuples = [("aditi", 1), ("tanya", 2)], Output_list_of_tuples = [("aditi", 1)]
'''
lt = []
list_of_tuples = [("aditi", 1), ("tanya", 2), ("John", 3), ("Emma", 4)]
vowels = set("aeiouAEIOU")
for name, roll in list_of_tuples:
    if name[0] in vowels:
        filtered_tuples = (name, roll) 
        lt.append(filtered_tuples)
print(lt)



