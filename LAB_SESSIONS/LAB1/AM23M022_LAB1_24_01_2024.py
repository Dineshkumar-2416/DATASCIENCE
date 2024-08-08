#!/usr/bin/env python
# coding: utf-8

# In[7]:


# 1.  WAP(Write a program) to find (print) the value of the following:

# 7*ln(3)*[ln(5)+ln(e^3)]



import math
answer_1 = 7*(math.log(3))*(math.log(5) + math.log(math.exp(3)))
print(answer_1)



# In[8]:


# Difference in area between two concentric circles of diameter 5m and 3m.

import math
radius1_sqred = (5/2)**2
radius2_sqred  = (3/2)**2
answer_2 = math.pi *(radius1_sqred - radius2_sqred)
print(answer_2  )


# In[9]:


# 2. WAP to return the count of odd numbers and even numbers between 7 and 80 (both inclusive) using arithmetic operators (without
# using loops) and print it using ‘format strings’ in a single line. (Refer to the attached file L3_output.py for examples of using
# formatted strings)


 
     
L = 7
R = 80
N = (R - L) // 2
 
# if either R or L is odd
if (R % 2 != 0 or L % 2 != 0):
 N += 1

odds = N
evens = (R - L + 1) - odds
print(f"Count of odd numbers is {odds} and Count of even numbers is {evens}")


# In[10]:


# 3. What are the different kinds of data types in python? Name them and explain their significance.WAP to demonstrate them in
# Python and print the size and type of each of them in ascending order.

"""

Numeric data types: int, float, complex

String data types: str

Sequence types: list, tuple, range

Binary types: bytes, bytearray, memoryview

Mapping data type: dict

Boolean type: bool

Set data types: set, frozenset"""

'''
Numeric Types:

int: Integer type represents whole numbers, e.g., 1, 100, -42.
float: Float type represents floating-point numbers with decimal parts, e.g., 3.14, -0.5.

Sequence Types:

str: String type represents sequences of characters, e.g., "hello", 'Python'.

list: List type represents ordered and mutable sequences, e.g., [1, 2, 3], ['apple', 'banana'].
tuple: Tuple type represents ordered and immutable sequences, e.g., (1, 2, 3), ('red', 'green').

Set Types:

set: Set type represents an unordered collection of unique elements, e.g., {1, 2, 3}, {'apple', 'orange'}.
Mapping Type:

dict: Dictionary type represents a collection of key-value pairs, e.g., {'name': 'John', 'age': 25}.
Boolean Type:

bool: Boolean type represents the truth values True or False.
None Type:

NoneType: The type of the None object, representing the absence of a value or a null value.
'''

import sys

def print_info(variable, name):
    return (name, sys.getsizeof(variable), type(variable))

# Numeric Types
integer_number = 42
float_number = 3.14

# Sequence Types
string_value = "Hello, Python!"
list_values = [1, 2, 3, 4, 5]
tuple_values = (10, 20, 30)

# Set Type
set_values = {1, 2, 3, 4, 5}

# Mapping Type
dictionary_values = {'name': 'John', 'age': 25}

# Boolean Type
boolean_value = True

# None Type
none_value = None

# Create a list of tuples
variables = [
    print_info(integer_number, "Integer"),
    print_info(float_number, "Float"),
    print_info(string_value, "String"),
    print_info(list_values, "List"),
    print_info(tuple_values, "Tuple"),
    print_info(set_values, "Set"),
    print_info(dictionary_values, "Dictionary"),
    print_info(boolean_value, "Boolean"),
    print_info(none_value, "None")
]

# Sort the list based on size
sorted_variables = sorted(variables, key=lambda x: x[1])


# Display information in ascending order of size
for var_name, var_size, var_type in sorted_variables:
    print(f"{var_name} - Type: {var_type}, Size: {var_size} bytes")


# In[14]:


# 4.  WAP to find the surface area of a cuboid with sides a,b,c. 
#The values of a, b, c  should be random numbers generated between 10 and 100. 
#Take the seed value as user input. (use ‘random’ module).

 
import random

seed_value = 22
random.seed(seed_value)

a= random.uniform(10,100)
b= random.uniform(10,100)
c= random.uniform(10,100)

surface_area= 2 * (a*b+b*c+c*a)
print(surface_area)


# In[16]:


# 5. WAP to solve the quadratic equation of the form ax^2+bx+c=0, 
# here a, b and c are real numbers and a ≠ 0 (Take a, b and c as user
# input)
import cmath

# Get user input for coefficients
a= float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

calcalution = b**2 - 4*a*c

# Check the nature of roots
if calcalution > 0 or calcalution<0 :
    # Two real and distinct roots or complex roots 
    root1 = (-b + cmath.sqrt(calcalution)) / (2*a)
    root2 = (-b - cmath.sqrt(calcalution)) / (2*a)
    print("Root 1:", root1)
    print("Root 2:", root2)
else:
    # One real root (both roots are the same)
    root = -b / (2*a)
    print("Root:", root)


# In[17]:


# 6. WAP to demonstrate various arithmetic operations by taking the two input numbers in a single line as space-separated-values (Use
# split function)

def add():
    return a+b
def subtract():
    return a-b
def multiply():
    return a*b
def divide():
    if b==0:
        return "cannot be divided by zero"
    return a/b

a,b= map(int,(input("enter two numbers").split(' ')))

print(f"addition:{add()},\n subtraction:{subtract()},\n multiplication:{multiply()},\n division:{divide()}")


# In[18]:


'''
7.Given the words ‘Learning’, ‘python’, ‘is’, ‘fun’. Accomplish the following tasks:
a. Create a sentence by combining these words : “Learning python is fun.” use(‘.join’)
b. Print the sentence “Learning datascience is fun.” (use ‘.replace’)
c. Generate an uppercase version of the sentence: “LEARNING PYTHON IS FUN.”
d. Rearrange the words to form a new sentence: “fun is python learning.”
e. Reverse each word in the sentence and print the result: “nuf si nohtyp gninrael.”
    '''

words =['Learning','python','is','fun']
combined= " ".join(words)
print(combined)
replacing= combined.replace('python','datascience')
print(replacing)
uppercase=combined.upper()
print(uppercase)
reversing=" ".join(words[::-1])
print(reversing)
print(combined[::-1])
# print("".join(reversed(combined)))


# In[9]:


# 9. What are ‘built-in-functions’ in Python? Explain any five

'''Python built-in functions are pre-defined functions that come bundled with Python and can be used directly in a Python program without importing external libraries
abs()	Returns the absolute value of a number
bool()	Returns the boolean value of the specified object
float()	Returns a floating point number
round()	Rounds a numbers
str()	Returns a string object
'''


# In[10]:


'''
8. How object oriented programming in Python is different from other object oriented languages?

Object-oriented programming (OOP) is a programming paradigm that is supported by many programming languages, and each language may implement OOP concepts in its own way. Python is an object-oriented language, and it shares many common OOP features with other languages. However, there are some differences and unique aspects to Python's implementation of OOP compared to other languages. Here are some key points:

Dynamic Typing:
Python is dynamically typed, meaning the type of a variable is determined at runtime. 
In Java or C++, variable types are declared explicitly at compile-time.
Dynamic typing in Python allows for more flexibility and ease of use

Multiple Inheritance:
Python supports multiple inheritance, allowing a class to inherit from more than one base class. 
Some other object-oriented languages, like Java, support single inheritance, meaning a class can inherit from only one superclass.

Object:
In Python, everything is an object, including integers, strings, and functions. 
This is different from some other languages where primitive types are not treated as objects.



'''


# In[20]:


'''
10. WAP to:
1. Count the number of vowels in a given string.
2. Check if a given string is palindrome.
'''
i = 0

def counting(lst):
    global i
    for char in lst:
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            i += 1

string = "DINESH KUMAR M Mtech"
counting(string)

print("Number of vowels", i)


word_check="malayalam"
if word_check[::]==word_check[::-1]:
    print("Palindrome")
else:
    print('Not a Palindroe')


# In[ ]:




