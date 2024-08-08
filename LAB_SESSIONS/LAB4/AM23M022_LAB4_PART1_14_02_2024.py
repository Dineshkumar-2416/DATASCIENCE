# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 14:04:43 2024

@author: mdine
"""

'''
1. Explore the use and syntax of common built-in functions: 

range(), 
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
Syntax
range(stop)
range(start, stop
range(start, stop, step)

x = range(6)
for n in x:
  print(n)

iter(), 
The iter() function returns an iterator object
Syntax
iter(object, sentinel)
object	- Required. An iterable object
sentinel- Optional. If the object is a callable object the iteration will stop when the returned value is the same as the sentine


x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))


eval(), 
The eval() function evaluates the specified expression, if the expression is a legal Python statement, it will be executed
Syntax
eval(expression, globals, locals)


expression- A String, that will be evaluated as Python code
globals- Optional. A dictionary containing global parameters
locals- Optional. A dictionary containing local parameters

x = 'print(55)'
eval(x)


enumerate(), 
The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.

The enumerate() function adds a counter as the key of the enumerate object.
Syntax
enumerate(iterable, start)
iterable- An iterable object
start- A Number. Defining the start number of the enumerate object. Default 0

x = ('apple', 'banana', 'cherry')
y = enumerate(x)


zip(), 
The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.

If the passed iterables have different lengths, the iterable with the least items decides the length of the new iterator
Syntax
zip(iterator1, iterator2, iterator3 ...)
iterable1, iterable2, iterable3 ...	Iterable objects that will be joined together

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)

lambda, 
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

Syntax
lambda arguments : expression

x = lambda a : a + 10
print(x(5))






input(), 
The input() function allows user input.
Syntax
input(prompt)
prompt- A String, representing a default message before the input

print('Enter your name:')
x = input()
print('Hello, ' + x)



map(),
The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
Syntax
map(function, iterables)

function- Required. The function to execute for each item
iterable- Required. A sequence, collection or an iterator object. You can send as many iterables as you like, just make sure the function has one parameter for each iterable.


def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))



filter(), 
The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not

Syntax
filter(function, iterable)

function- A Function to be run for each item in the iterable
iterable- The iterable to be filtered

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)
  
  


next()
The next() function returns the next item in an iterator.

You can add a default return value, to return if the iterable has reached to its end




Syntax
next(iterable, default)
iterable- Required. An iterable object.
default- Optional. An default value to return if the iterable has reached to its end.
mylist = iter(["apple", "banana", "cherry"])
x = next(mylist)
print(x)
x = next(mylist)
print(x)
x = next(mylist)
print(x)



reduce()

The reduce() function accepts a function and a sequence and returns a single value calculated as follows:

Initially, the function is called with the first two items from the sequence and the result is returned.
The function is then called again with the result obtained in step 1 and the next value in the sequence. This process keeps repeating until there are items in the sequence.


Syntax: reduce(function, sequence[, initial]) -> value


from functools import reduce
def do_sum(x1, x2): return x1 + x2
reduce(do_sum, [1, 2, 3, 4])



Include a short description and a practical code example for each, ensuring clarity through comments
'''
'''
2. Write a Python function that sorts a dictionary based on the length of values.

Sample:

Input: {'lemon':'yellow','apple':'red'} output: {'apple':'red','lemon':'yellow'}

people = {3: "Jimeeee", 2: "Jack", 4: "Janee", 1: "Jilel"}
print(dict(sorted(people.items(), key=lambda item: item[1])))
'''




dictionary ={3: "Jimeeee", 2: "Jacke", 4: "Janeee", 1: "J"} 
sorted_dict = dict(sorted(dictionary.items(), key=lambda item: len(item[1])))
print(sorted_dict)

'''

3. Develop a Python program that executes the following tasks with a user-provided string:

a. Prompt the user to input a string.

b. Create a dictionary from the string where each key is a unique alphabet character and the corresponding value is the frequency of that character's occurrence in the string.

c. Generate a sorted list of tuples from the dictionary based on character frequency (values).

d. Generate a sorted list of tuples from the dictionary based on the alphabet characters (keys).

e. Identify the three most frequently occurring characters. In the event of a frequency tie, prioritize characters in lexicographical order.

Your program should showcase proficiency in dictionary operations, sorting mechanisms, and handling of ties in frequency counts. Comment your code to outline the process and decisions made.

sample:

input = 'GOOGLE'

Here, the most repeated characters are G:2, O:2. But, L,E are occurring only a single time which is tied for the third position here, so here we take E as it comes first in the lexicographical order.

'''
#Getting input from the user
a_dict = {}
# a_dict['key'] = 'value'
dic = input("Enter a word: ")

# b

for  i in dic:
    value = dic.count(i)  
    a_dict[i] = value
    
print(a_dict)



# Sort the dictionary based on character frequency
sorted_by_freq = dict(sorted(a_dict.items(), key=lambda item: item[1]))
print(sorted_by_freq)


# Generate a sorted list of tuples based on alphabet characters (keys)
sorted_by_char = sorted(a_dict.items())

print(sorted_by_char)



# Sort the dictionary based on character frequency (with ties broken by lexicographical order)
sorted_by_freq = sorted(a_dict .items(), key=lambda item: (-item[1], item[0]))
print(sorted_by_freq)
# Identify the three most frequently occurring characters
# most_freq_chars = sorted_by_freq[:3]

# print(most_freq_chars)


'''
4. Write a function called lookup_student that takes a dictionary representing student records, where names are keys and roll numbers are values. The function should search for a specified student name and return the corresponding roll number if found; otherwise, it should return "Not Found" 

Example:

records = { "Alice" : "AB111", "Bob" : "EE200", "David" : "XY333"}

print(lookup_student(records, "Bob")) : Should print "EE200"

print(lookup_student(records, "John")) : Should print "Not Found"

'''

def lookup_student(records, name):
    
    if name in records:
        
        return records[name]
    else:
        return "Not Found"


records = { "Alice" : "AB111", "Bob" : "EE200", "David" : "XY333"}
print(lookup_student(records, "David")) 
print(lookup_student(records, "ff")) 



'''

5. Given a list of integers, write a Python program to:

a) Find the frequency of each integer in the list and store the result in a dictionary.

b) Print the maximum integer and its frequency.

c) Remove duplicates from the list and print the new list without changing the order of elements. Do this operation without using the set data type.

d) Remove duplicates from the list and print the new list. Do this operation using the set data type.

'''

# Given list of integers
numbers = [2, 3, 4, 2, 3, 5, 6, 3, 4, 5, 7, 8, 5, 4]
 # Step a: Find the frequency of each integer and store the result in a dictionary
freq_dict = {}
for num in numbers:
   value = numbers.count(num)
   freq_dict[num] = value
print(freq_dict)
   
 # Step b: Print the maximum integer and its frequency
max_num =max(numbers)
print(max_num)
print(freq_dict[max_num])


# Step c: Remove duplicates from the list without changing the order of elements
unique_list = []
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)
        
print(unique_list)
# Remove duplicates from the list using set data type
print(list(set(numbers)))






