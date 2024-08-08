# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:04:45 2024

@author: mdine
"""

'''
2. Write a program using list comprehension

a) To add the corresponding elements of two lists and print the new list.

b) To perform element wise multiplication of two lists and print the new list.

c) To create a list of the unique characters of a given string. 

Eg: input = “hello” , output = [‘h’, ‘e’, ‘l’, ‘o’]
'''
# a) To add the corresponding elements of two lists and print the new list.
com_list=[]
lst1 = [2,4,6,8]
lst2 = [1,3,5,7]
com_lst = [lst1[i] + lst2[i] for i in range(0,len(lst1)) ]
print(com_lst)

# b) To perform element wise multiplication of two lists and print the new list.
ele_mul = com_lst = [lst1[i] * lst2[i] for i in range(0,len(lst1)) ]
print(ele_mul )

# c) To create a list of the unique characters of a given string. 
input_string = "dineesh"
emp = []
for i in input_string:
    if i not in emp:
        emp.append(i)

print(emp)

'''
3. Using the zip function, WAP

a) To add the elements of 2 matrices (Define matrices as per your wish).

b) To perform element wise multiplication on 2 matrices.
'''



# a) To add the elements of 2 matrices (Define matrices as per your wish).
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result_addition = []
for row1, row2 in zip(matrix1, matrix2):
    print (row1)
    print(row2)
    result_row = [x + y for x, y in zip(row1, row2)]
    result_addition.append(result_row)
print("result_addition", result_addition)
# b) To perform element wise multiplication on 2 matrices.
result_multiplication = []
for row1, row2 in zip(matrix1, matrix2):
    result_row = [x * y for x, y in zip(row1, row2)]
    result_multiplication.append(result_row)
print("result_multiplication", result_multiplication)

'''
4. List of List : Given a square matrix represented as a list of lists, 

a) WAP to print the row sum, column sum and trace of the matrix 

b) WAP to print the transpose of the matrix.

c) WAP to check whether the given matrix is symmetric or not.

d) WAP to check whether the Identity matrix (I) is positive definite or not by using Quadratic form method (x^T*I*x > 0), where x is any non zero vector.

'''
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# a) WAP to print the row sum, column sum and trace of the matrix 
# for i in matrix1:
#     ele = 0
#     for j in i:
#       ele +=j
#     print("row_sum", ele)
row_sums = [sum(row) for row in matrix1]
print("row_sums" ,row_sums)
n = len(matrix1)    
col_sums = [sum(matrix1[i][j] for i in range(n)) for j in range(n)]
print("Column_sum" ,col_sums)

trace = sum(matrix1[i][i] for i in range(n))
print("trace" ,trace)

transpose = [[matrix1[j][i] for j in range(len(matrix1))] for i in range(len(matrix1))]
print("Transpose:", transpose)


if matrix1 == transpose:

    print("the matrix is symmetric.")
else:
    print("the matrix is not symmetric.")



def is_positive_definite_identity_matrix(I):
    n = len(I)
    x = [1] * n  # We choose a vector of ones for simplicity
    print(x)
    quadratic_form = sum(x[i] * I[i][j] * x[j] for i in range(n) for j in range(n))
    print(quadratic_form)
    return quadratic_form > 0

# Example: Identity matrix (I)
identity_matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

# Check if the identity matrix is positive definite
if is_positive_definite_identity_matrix(identity_matrix):
    print("The Identity matrix is positive definite.")
else:
    print("The Identity matrix is not positive definite.")

    
'''
5.  List of Lists : WAP to remove sub lists from a given list of lists that contain an element outside a given range.

Example :

Input : [[3], [1, 3, 2], [0, 1, 9, 3, 5, 7], [9, 10], [13, 14, 16, 17]]  Range: 1, 5

Output : [[3], [1, 3, 2]]

Explanation : If a sublist has a number that is other than 1, 2, 3, 4, 5, remove the sublist from the list of lists and print the remaining sublists as a lists of lists    

'''



res = []
input_list = [[3], [1, 3, 2], [0, 1, 9, 3, 5, 7], [9, 10], [13, 14, 16, 17]]


for sublist in input_list:
    include_sublist = True
    for num in sublist:
        if not (1<= num <= 5):
            include_sublist = False
            break
    if include_sublist:
        res.append(sublist)

print(res)

'''
1.Write a program (WAP) to implement the following operations on a collection of library books:

(a) Construct a catalog of books, with each book having an author's name, book title, ISBN number, publication year, and number of pages.

(b) Add a new book to the catalog, ensuring that the books are kept in ascending order based on the publication year.

(c) Locate a book by its ISBN number and delete the book's entry from the catalog.

(d) Insert a new book entry at the end of the catalog using the provided book information.

(e) Identify and remove any duplicate entries in the catalog, preserving only one copy of each book based on its ISBN number.

(f) Reorganize the entire catalog so that the books are sorted in descending order by the number of pages

'''
library = []

# Construct a catalog
book1 = {"author": "kavi", "title": "discipline", "isbn": "123456789", "publication_year": 2000, "num_pages": 200}
book2 = {"author": "dinesh", "title": "hardwork", "isbn": "234567890", "publication_year": 1990, "num_pages": 300}
book3 = {"author": "rohit", "title": "consistency", "isbn": "345678901", "publication_year": 2010, "num_pages": 150}

if not library:
    library.append(book1)
else:
    for i, b in enumerate(library):        
        if book1["publication_year"] < b["publication_year"]:
            library.insert(i, book1)
            break
    else:
        library.append(book1)

if not library:
    library.append(book2)
else:
    for i, b in enumerate(library):
        if book2["publication_year"] < b["publication_year"]:
            library.insert(i, book2)
            break
    else:
        library.append(book2)

if not library:
    library.append(book3)
else:
    for i, b in enumerate(library):
        if book3["publication_year"] < b["publication_year"]:
            library.insert(i, book3)
            break
    else:
        library.append(book3)
print("sorting based on th publication year")        
print(library)
print("\n")


print("Adding a new book")
new_book = {"author": "athul", "title": "forrest_gump", "isbn": "456789012", "publication_year": 2020, "num_pages": 250}
if not library:
    library.append(new_book)
else:
    for i, b in enumerate(library):
        if new_book["publication_year"] < b["publication_year"]:
            library.insert(i, new_book)
            break
    else:
        library.append(new_book)

print(library)
print("\n")

print("Locate and delete a book")

isbn_to_delete = "234567890"
for i, book in enumerate(library):
    if book["isbn"] == isbn_to_delete:
        del library[i]
        break


print(library)
print("\n")

print("Inserting a new book entry at the end")
new_book_at_end = {"author": "sushant", "title": "atomic habits", "isbn": "567890123", "publication_year": 2005, "num_pages": 180}
library.append(new_book_at_end)

print(library)
print("\n")

print("Remove duplicates")
seen_isbns = set()
unique_library = []
for book in library:
    if book["isbn"] not in seen_isbns:
        unique_library.append(book)
        seen_isbns.add(book["isbn"])
library = unique_library

print(library)
print("\n")

print("Reorganizing based on the number of pages")
for i in range(len(library)):
    for j in range(i + 1, len(library)):
        if library[i]["num_pages"] < library[j]["num_pages"]:
            library[i], library[j] = library[j], library[i]

print(library)
print("\n")
