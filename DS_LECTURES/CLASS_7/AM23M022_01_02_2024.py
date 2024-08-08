# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 10:02:55 2024

@author: mdine
"""
'''
Tuple container
'''

tup1 =()
print(type(tup1))
tup=(10)
print(tup)
print(type(tup))
tup2 = (10,)
print(tup2)
print(type(tup2))


# tuple basics and accessing
# can be indexed and sliced
tp = (2,5,8)
# print(tp[0:])
# Entire tuple or each element can be printed.
# Tuple is an `iterable’ i.e. you can iterate over its elements.
for i  in tp:
    print(i)
    
# Tuples are immutable (like strings).
tp = (2,5,8)
tp[0] = 9
print(tp ) #'tuple' object does not support item assignment

tp = (25,88,32,5,8)
tp1 = sorted(tp)
print(tp1 ) 

# tuple comparison
# using relational operation
tp = (25,88,32,5,8)
tpp = ('DK',2,4)

if tp  == tpp:
    print("YES")
else:
    print("NO")
    
#Tuple Comprehension

tppp = tuple([num for num in range(1,10)])
print(tppp)

tppp = [num for num in range(1,10)]
print(type(tppp))



    
    
# Tuple Varieties

# TUPLE OF TUPLE

tup_comp = tuple([(x**2, x**3) for x in range(5)])
print('Tuple from a list comprehension : ', tup_comp)

for i in tup_comp:
    print(i)

# Tuple embedding
ts = (1,2,3,4)
tw = (5,ts,8,9)
#  Tuple unpacking (using * operator)
tx = (4,*ts)
print(tw)
print(tx)

print(list(tx))
print(tuple(list(tx)))
str1 = ' dinesh'
for a in str1:
    print(tuple(a)) #cant be appended 
    '''(' ',)
    ('d',)
    ('i',)
    ('n',)
    ('e',)
    ('s',)
    ('h',)'''
    
# Grouping Tuples
# Taking one each from each tuple

names = ('Ram', 'Raja', 'Geetha', 'Ramya')
gender = ('male', 'male', 'female', 'female')

# tpp = tuple((i + j ) for i in names for j in gender )
# print(tpp)

l = (names[0], gender[0]), (names[1], gender[1]),(names[2], gender[2]),(names[3], gender[3])
print(l)          



for i in range(len(names)):
    t = tuple([names[i] +" " + gender[i]])
    print(t)
tp = tuple(zip(names,  gender))
print(tp)

