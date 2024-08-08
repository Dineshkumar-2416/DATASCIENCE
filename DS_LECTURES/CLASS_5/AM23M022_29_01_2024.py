#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Container
# They can hold multiple data types.
# • Lists, Tuples, Sets, Dictionaries
# • Also called as collections / compound data types



# In[7]:


# List
# List is a collection of dissimilar data types (mostly used for similar datatype)
lst1= [1,4,8, ' KAVI']
print(lst1)
#Index
print(lst1[0])


# In[6]:


lst4 = [100] * 5
print(lst4)


# In[8]:


# List is an `iterable’


# In[9]:


# List contatiner - few examples

lst1 = [10, 200, 300, 40]

lst2 = ['cow', 'bull', 'tiger', 'lion', 'rhinoceros', 'antelope']

lst3 = [12.5, 6.5, 7.45, 6.456, 6.5, 2.34, 5.78, 8.95, 1.2345]

#Mixed datatype list
lst4 =  [12, 45.4, 'Raman']

#Empty list using square brackets
lst5 = []

#Printing a full list - just give the name of the list

print(type(lst1),lst1)


# In[10]:


print(lst1[1:])


# In[11]:


print('Printing a portion of a list - slicing')
print(lst1[1:3])
print(lst1[1:])


# In[12]:


#List is Iterable. You can iterate over the list

print('Printing the elements of lst1')
for i in lst1:
    print(i)
    
print('Printing the elements of lst2')
for i in lst2:
    print(i)

print('Printing the elements of lst3')
for i in lst3:
    print(i)
    
print('Printing the elements of lst4')
for i in lst4:
    print(i)
    
print('Printing the elements of lst5')
for i in lst5:
    print(i)


# In[13]:


# HW: List and Array difference in terms of memory allocation
#No of vowels in strings


# In[14]:


# CW: Define a list of strings and find the 
# number of characters in each of them

ListA = ["DK", "LA"]
print(len(ListA[0]))

#difference between count and length?


# In[15]:


ListA = ["Dinesh", "Kaviyarasan"]
ListA[0] = "GK"
print(ListA)


# In[24]:


# Lists can be concatenated
ListA = ["Dinesh", "Kaviyarasan"]
lst1 = [10, 200, 300, 40]
Lst = ListA + lst1
print(Lst)
# deletion - using index or range of indices
# Lst[0] = []
# print(Lst)  - [[], 'Kaviyarasan', 10, 200, 300, 40]
Lst.pop(0)
print(Lst)


# In[26]:


#Member function and Built in function difference?
# searching (containment) and sorting
#searching (containment) and sorting - in and not in functions
lst = [10, 20, 30, 40, 50]
print(lst)
lst[0] = 100
print('muted list', lst)
lst[2:5] = [300, 400, 500]
print('muted list', lst)

#different way of deleting
lst[:] = []
print('deleting using empty list symbol', lst)

#Lists concatenation
lst1 = [6, 7, 8, 9]
lst += lst1
print('concatenated lists:', lst)
print('a' in ['a', 'e', 'i'])
print('b' in ['a', 'e', 'i'])

vow_lst = ['o', 'a', 'e', 'i']
vow_s_lst = sorted(vow_lst) # does not change the original list

print('original list is ', vow_lst, ',', 'sorted list is ',vow_s_lst)
print(type(vow_s_lst))

#Deleting using del function
del(vow_lst[2])
print('List after deleting index 2 element is :',vow_lst)
del(vow_lst[:])
print('List after deleting all elements is :',vow_lst)


# In[21]:


lst = [10, 20, 30, 40, 50]
print(lst)
lst[0] = 100
print('muted list', lst)
lst[2:5] = [300, 400, 500]
print('muted list', lst)

#different way of deleting
lst[:] = []
print('deleting using empty list symbol', lst)


# In[36]:


# Define a list of marks for a student and find the 
# max, min and average of them. Arranged the in sorted 
# order. Print all of them clearly. Delete the entire list and 
# check for emptiness.

Marks = [75,56,89,35,98,44]
print(min(Marks))
print(max(Marks))
len(Marks)
total = 0
for ind in Marks:
    total += ind
Average = total / len(Marks)
print(Average)
print(sorted(Marks ))
Marks [:] = []
print('deleting using empty list symbol', Marks)

     
    


# In[38]:


lst = [10, 30, 20, 15, 20, 60, 80, 70]

print('Printing the list', lst)

lst.append(23)

print('Printing the list after appending', lst)

lst.pop()

print('Printing the list after pop()', lst)

lst.pop(3)

print('Printing the list after popping 4th element', lst)

lst.sort()

print('Printing the list after sorting', lst)

lst.remove(20)

lst.insert(3, 34)   

print('Printing the list after insertion', lst)

print('number of occurances of 20: ',lst.count(20))

print('index of number 20: ', lst.index(10))

lst.sort(reverse=True)

print('Printing the list after sorting', lst)

lst.reverse()

print('Printing the list after sorting in reverse', lst)



# In[ ]:


# Object oriented programming
# fn overloading and operator overloading
#same fn but different argument?
# polymorphism

