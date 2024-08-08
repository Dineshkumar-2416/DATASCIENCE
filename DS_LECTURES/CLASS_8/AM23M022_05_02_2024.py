# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 12:00:25 2024

@author: mdine
"""

# 2*3 matirx and perform transpose

mat = [[1,2,3], [4,5,6]]
print(mat[0], mat[1])
for ite in zip(mat[0], mat[1]):
    print('Each tuple in zip = ', ite, 'sum of the each tuple = ', sum(ite))
    print('Priting the elements of each tuple using index ', ite[0], ite[1])
    print('same result as above but using unpacking', *ite)

print(mat[0], mat[1]) 
print(*mat)
for it in zip(*mat):
    print(sum(it))
    
#Matrix inverse
ite = zip(*mat)
lst = list(ite)
print('Matrix inverse = ', lst)


mat1 = [[20,30,40], [50,60,70]]
print(mat1)
ite = zip(mat, mat1)
print(*ite)
mat2 = [[sum(a) for a in zip(*b)] for b in zip(mat, mat1)]
print(mat2)

#  2 matrix perform +, - , * , Inverse
#Dict and hashtable

''' SET '''
# Create a new set:
    
f = {}
print(type(f))  '''<class 'dict'>'''
print("Create a new set:")

# Initialize an empty set and assign it to the variable 'x':
x = set()

# Print the empty set 'x':
print(x)

# Print the data type of 'x', which should be 'set':
print(type(x))

# It is an unordered collection - cannot be indexed and sliced
# FROZENSET ???

# conversion / other functions - len, max, min, sum, sorted
k = set()
j = {5,3,8,88}
set(sorted(j))
print(set(sorted(j)))

'''
Given a set S, you can apply the following member functions using the object 
(syntax - S.func( )).
• add - at the end
• remove - the element
• discard - what is the difference between remove and discard?
• clear - clears all the elements
'''

#Sorted and unsorted set in python and in another language
j = {5,3,8,88}
# j.remove(99)
#print(j) # KeyError: 99

j.discard(99)
print(j)
#UPDATE
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft"}

x.update(y) 

print(x)
'''
Given two sets S and T, you can apply the following member functions.
• update - adds elements of one list to the other (E.g. S.update(T))
• issuperset 
• issubset
• isdisjoint
• comparison of two sets using relational operators
'''

'''
Set of Sets is not allowed, in general, can be done using frozenset
• Set embedding is not allowed
• Set unpacking (using * operator) Ramanat
'''
'''Set embedding is not allowed'''
k = {5,9,4}
dd= {99,k,77}
 print(dd)  #unhashable type: 'set'
 
#Set unpacking (using * operator) 
k = {5,9,4}
dd= {99,*k,77}
print(dd)

'''Set Comprehension'''
k = {5,9,4}
dd= {99,8,77}
tt = {i+j for i in k for j in dd }
print(tt)

'''Create a set consisting of squares of 
integers from 1 to 9 using set 
comprehension'''
seta = {y** 2 for y in range (1,10)}
print(seta)