# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 17:26:01 2024

@author: mdine
"""

# List varieties
# List of lists

a = [1,2,3,4,5]
b = [11,12,13,14,15]
c = [a, b]
print('list of lists',c)

#individual elements accessing - similar to 2D array
print('some list elements: ',c[0][0], c[1][0], c[0][4], c[1][4])

#List embedding
x = [1, 2, 3, 4]
y = [10, 11, x, 13]
print('Embedded list',y, type(y))

#List unpacking
x = [1, 2, 3, 5]
y = [10, 11, *x, 13]
print('Unpacked list',y, type(y))


lst = []
for var in range(0,11):
    lst.append(var)
print(lst)

lst = [var for var in range(0,11)]
print(lst)



#On list of lists - 2D array

arr = [[1,2,3,4], [5,6,7,8]]
print('What will be the answer to the following?')
print('arr = ', arr, '*arr = ', *arr)
print('What are your observations?')

print('What will be the answer to the following?')
print('arr[0] = ', arr[0], 'arr[1] = ', arr[1])
print('*arr[0] = ', *arr[0], '*arr[1] = ', *arr[1])
print('What are your observations?')

#To get the number of rows and columns
print('number of rows = ', len(arr))
print('number of columns = ',len(arr[0]))

arr_lst = []
for ele in arr:
    print('elements of each row', ele)
    for num in ele:
        arr_lst.append(num)
        
print(arr_lst)

arr_lst1 = [num for ele in arr for num in ele]
print(arr_lst1)


n1 = []
arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
for ele in arr:
    # print(ele)
    for num in ele:
        print(num)
        n1.append(num)
print(n1)

 