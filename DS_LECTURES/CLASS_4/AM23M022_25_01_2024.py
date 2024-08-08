#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Relational operators 
# Relational operators in Python programming are also known as comparison operators. They serve the basic purpose of conducting relational operations, i.e., comparisons between two operands. They hence facilitate the decision-making process in a program. Other uses of relational operators include controlling the program flow, filtering data, etc. These operators can be used with numerical values, strings, and objects
# Relational operators
# almost same as C
# • < 
# • > 
# • <= 
# • >=
# • ==
# • !=


# Python Logical Operators

# Logical operators are used to combine conditional statements:
# Operator 	Description 	Example 	Try it
# and  	Returns True if both statements are true 	x < 5 and  x < 10 	
# or 	Returns True if one of the statements is true 	x < 5 or x < 4 	
# not 	Reverse the result, returns False if the result is true 	not(x < 5 and x < 10)


# In[ ]:


a, b, c = input('Enter two values a and b and  c : ').split()
a = int(a)
b = int(b)
c = int(c)

# if a==b==c:
#     print("All three are Equal")
# else:
#     print("Not equal")

if a!=b!=a:
    print("All three are Equal")
else:
    print("Not equal")


# In[ ]:


a, b = input('Enter two values a and b: ').split()
a = int(a)
b = int(b)

#print(a is b)

if a<b:
    print('a less than b')
else:
    print('a greater than or equal to b')


# In[ ]:


# Logical operators
# and, or, not (NOT &&, ||, ! but works similarly)
# • cond1 and cond2 - returns True only if both are true
# • cond1 or cond2 - returns True if even one of the is true.
# • NOTE: We can replace ‘condition’ with any ‘valid expression’


# In[ ]:


# how printf and scanf work not using any function protocol?


# In[ ]:


#Conditional expression
# HW: Redo the largest one including logical 
# operators.
dk= a if a > b else b
print('Largest one is ', dk)


# In[ ]:


# HW: Also, get to know about the functions any( ) 
# and all( )

# The any() function returns True if any element of an iterable is True. If not, it returns False.

# mylist = [False, True, False]
# x = any(mylist)
# print(x)

boolean_list = ['True', 'False', 'True']

# check if any element is true
result = any(boolean_list)

print(result)

# Output: True


# In[ ]:


# The all() function returns True if all elements in the given iterable are true. If not, it returns False
# mylist = [True, True, True]
# x = all(mylist)
# print(x)

boolean_list = ['True', 'True', 'True']

# check if all elements are true
result = all(boolean_list)

print(result)

# Output: True


# In[ ]:


# Loops
# while and for (No do-while) - there are differences


# In[ ]:


# WHILE
i = 1
while i < 6:
  print(i)
  i += 1


# In[ ]:


# Key differences between for and while
# • for iterates over the iterable (string/ list etc..), where as while does not
# • while uses a condition where as for does not
str1 = "Raman"
for ele in str1:
    print(ele)
    
    
# str1 = "Raman"
# while ele in str1:
#     print(ele)


# In[ ]:


# range( ) function


# In[ ]:


# HW: Find about break, continue, and pass statements and 
# use them in a program. 
# HW: Print numbers 1 to 10 on the same line, breaking out of 
# an infinite loop. 
# HW: Print all unique combinations of 1, 2 and 3.

# HW: Conditional expression - Ternary operator in python and in c (?:)

