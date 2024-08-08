# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:17:14 2024

@author: mdine
"""

# 2. Number 34567222541147 has been given. Print the addition of all even digits and the addition of all odd digits.
# [Sample input = 156893, Sample Output: sum_even = 14 , sum_odd = 18]
 
num = 156893
# print(num[0])
# 'int' object is not subscriptable
# to access the digit of the number, convert it to string
num_str = str(num)
sum_even = 0
sum_odd = 0
for i in num_str:
    i = int(i)
    if i % 2 == 0:
        sum_even += i
        
    elif i % 2 != 0:
        sum_odd += i
print(sum_even) 
print(sum_odd)  


# 1. Write a program to print numbers divisible by both 7 and 8. Numbers between 1 and 1000.
# [Numbers like 56, which are both divisible by 7 and 8]
# a. Using continue statement
# b. Using the pass statement

print("Numbers divisible by both 7 and 8 between 1 and 1000 Using Pass Statement:")
for j in range(1,1001):
    if j%7==0 and j%8==0:       
        print(j)
    else:
        pass
print("Numbers divisible by both 7 and 8 between 1 and 1000 Using Continue Statement:")
for j in range(1, 1001):
    if j % 7 != 0 or j % 8 != 0:
        # print(j)
        continue
        # print(j)
    print(j)
    
    
# 3. Describe conditional expression. Write a program to print the maximum and minimum numbers from a list using conditional expression. Usethe max () and min () functions to verify your output.

max_num = 0
lst = [25, 36, 55, 56, 99, 198, 1]   
for t in lst :
    if max_num < t :
        max_num = t
print(max_num)
lst = [25, 36, 55, 56, 99, 198, 1]   
min_num = lst[0] 
for t in lst :
   if t < min_num :
       min_num = t
print(min_num) 

#Pascal’s  Triangle : Print the following pattern for the given N number of rows.

# Pattern for N = 8      
    
def print_pascals_triangle(n):
    for i in range(n):
        # Calculate the value of the elements in the current row
        num = 1
        for _ in range(n - i - 1):
            print(" ", end=" ")  # Print leading spaces for alignment
        for j in range(i + 1):
            
            print(num, end="   ")  # Adjust the spacing for alignment
            num = num * (i - j) // (j + 1)
        print()

# Define the number of rows for Pascal's triangle
num_rows = 7

# Print Pascal's triangle with spacing alignment
print_pascals_triangle(num_rows)  
    
# 5. A palindrome sentence is a phrase or sentence that reads the same forward as it does backward, ignoring spaces, punctuation, andcapitalization.
# A) Take a number as input, determine if it is a palindrome, considering only numeric characters. Eg: 2442
# B) Now, take a string as an input and check whether it is Palindrome or not.  eg: "Was it a car or a cat I saw?"      
    
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    # print(dig)
    rev=rev*10+dig
    print(rev)
    n=n//10
    # print(n)
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
    
    
def is_palindrome(string): 
    processed_string = string.lower().replace(" ", "") 
 
    # Set pointers for comparison 
    start = 0 
    end = len(processed_string) - 1 
 
    # Check if characters from start and end match 
    while start < end: 
        if processed_string[start] != processed_string[end]: 
            return False 
        start += 1 
        end -= 1 
 
    return True 
 
# Test cases 
input_string1 = "Was it a car or a cat I saw " 

print(is_palindrome(input_string1))


'''
6. Describe chr () and ord () functions. Write a small program to show its functionality.Using these functions,write a program to print:
Pattern for N=4
  A
  B B
  C C C
  D D D D 
'''


N= int(input("Enter the number : "))
first = ord("A")
# print(first)

for z in range(N):
    # print(z)
    print((chr(first+z) + " ") * (z+1))
    
'''
7.You have a single list of names (each name should have first name and last name). Write a programme
(a) to print the first names.
(b) to print the last names.
(c) to print each name as 'last_name first_name.

(d) to print the names in the sorted order with respect to last name
Example :Input list: ['Mark Antony', 'Mohan Raj'],
Output :
 a) ['Mark', 'Mohan']  
b) ['Antony', 'Raj'] 
c) ['Antony Mark', 'Raj Mohan']
d) ['Mark Antony', 'Mohan Raj'] '''
    
Input_lst = ['Mark Antony', 'Mohan Raj', 'Dinesh Kumar']
first = []
last = []
com = []
for k in Input_lst:
    first_name, last_name = k.split() 
    first.append(first_name)
    last.append(last_name)
print (first)
print(last)

# (c) to print each name as 'last_name first_name.
for i in range(len(first)):
    v = last[i] +" "+ first [i]
    com.append(v)
print(com)

# (d) to print the names in the sorted order with respect to last name
Input_lst = ['Mark Antony', 'Mohan Raj', 'Dinesh Kumar']
sorted_names = []

for last_name_to_check in sorted(last):
    for name in Input_lst:
        if name.split()[1] == last_name_to_check:
            sorted_names.append(name)

print("Sorted names with respect to last name:", sorted_names)

''' 
8. WAP to find the minimum of 3 numbers using
 a) with conditional expressions. (No loops should be used)
 b) with nested conditional expression. (No loops should be used)
 c) similar to problem (b), find the minimum of 4 numbers.
    
'''
    
# a) with conditional expressions. (No loops should be used)
    
num1,num2,num3 = input("Enter 3 numbers : ").split()
if num1<num2:
    if num1<num3:
        print("Min is : " ,num1)
    else:
        print("Min is : " ,num3)
    
else:
    if num2<num3:
        print("Min is : " ,num2)
    else:
        print("Min is : " ,num3)

#  b) with nested conditional expression. (No loops should be used)

def min_of_three(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c

num1,num2,num3 = input("Enter 3 numbers : ").split()
result = min_of_three(num1, num2, num3)
print("The minimum of the three numbers is: ", result)

# c) similar to problem (b), find the minimum of 4 numbers.
def min_of_four(a, b, c, d):
    if a <= b and a <= c and a <= d:
        return a
    elif b <= a and b <= c and b <= d:
        return b
    elif c <= a and c <= b and c <= d:
        return c
    else:
        return d

num1,num2,num3,num4 = input("Enter 4 numbers : ").split()

result = min_of_four(num1, num2, num3, num4)
print("The minimum of the four numbers is: " , result)

'''
9. Create a list of departments in IIT Madras (Minimum 5 ) and perform the following operations:
 append
remove pop
insert  reverse
sort
count
index
extend
slice
clear

'''


iit_departments = ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering", "Chemical Engineering"]

#  append
iit_departments.append("Biomedical Engineering")
print("Appending Biotechnology:", iit_departments)

# remove pop
iit_departments.remove("Civil Engineering")
print("Removing Civil Engineering:", iit_departments)

popped_department = iit_departments.pop()
print("Popped department: ", popped_department)
print("Popping the last department:", iit_departments)

# insert  reverse
iit_departments.insert(1, "Aerospace Engineering")
print("Inserting Aerospace Engineering at index 1:", iit_departments)

iit_departments.reverse()
print("Reversing the list:", iit_departments)

# Sort 
iit_departments.sort()
print("Sorting the list:", iit_departments)

# Count 
count_cse = iit_departments.count("Computer Science")
print("Count of Computer Science: ", count_cse)

#  index 
index_mech = iit_departments.index("Mechanical Engineering")
print("Index of Mechanical Engineering: ", index_mech)

# Extend 
additional_departments = ["Mathematics", "Physics"]
iit_departments.extend(additional_departments)
print("Extending the list with Mathematics and Physics:", iit_departments)

# Slice
sliced_list = iit_departments[2:5]
print("Sliced list from index 2 to 4:", sliced_list)

# Clear
iit_departments.clear()
print("Clearing the list:", iit_departments)

    
    


    



    

 
