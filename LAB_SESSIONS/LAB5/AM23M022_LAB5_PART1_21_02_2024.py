# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 14:10:01 2024

@author: mdine
"""
'''
1. Write a program(WAP) using loops and recursion: 

a) Factorial of n where n is a non negative integer. 

b) For calculating the Nth Fibonacci number.

c) To calculate a^b where a>0, b>=0.
    
 '''
 
''''Using recursion '''
def factorial(n):
     print(n)
     if (n==1 or n==0) :
         return 1 
     
     c = n * factorial(n - 1) 
     
     return c
 
num = 5
print(factorial(num))


'''using loops'''
def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        while(n > 1):
            factorial *= n
            n -= 1
        return factorial
 

num = 5
print("Factorial of",num,"is",
factorial(num))


'''Using recursion '''
def Fibonacci(n):
    
    if n<= 0:
        print("Incorrect input")
    
    elif n == 1:
        return 0
    
    elif n == 2:
        return 1
    else:
        
        return Fibonacci(n-1)+Fibonacci(n-2)
 

print(Fibonacci(10))

'''using loops'''
a, b = 0, 1

n = 10

for i in range(n):

   # print(a,b)

   a, b = b, a + b
print(a)

'''Using recursion '''


def power_recursive(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * power_recursive(a, b - 1)

# Using loop
def power_loop(a, b):
    result = 1
    for _ in range(b):
        result *= a
        print(result)
    return result


a = 5
b = 9
print(power_recursive(a, b))
print(power_loop(a, b))


'''
3. Programs using lambda function.

a) Given a list of names, use map to create a list where each name is prefixed with "Hello, ".

Example Input: ['Alice', 'Bob', 'Charlie']
Example Output: ['Hello, Alice', 'Hello, Bob', 'Hello, Charlie']
'''


names = ['Alice', 'Bob', 'Charlie']
greeted_names = list(map(lambda name: f'Hello, {name}', names))
print(greeted_names)

'''
b) Use filter and a lambda function to extract all even numbers from a given list.

Example Input: [1, 2, 3, 4, 5, 6]
Example Output: [2, 4, 6]
'''

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


'''
c) Use reduce and lambda to concatenate all strings in a given list.

Example Input: ['Python', 'is', 'awesome']
Example Output: 'Pythonisawesome'
'''

from functools import reduce

strings = ['Python', 'is', 'awesome']
concatenated_string = reduce(lambda x, y: x + y, strings)
print(concatenated_string)

'''
2. Query for 2 integers N and M from the user where 0<=N<=100 and 0<=M<=9. These will be the inputs to your function. Using recursion, compute the number of times the integer M occurs in all non-negative integers less than or equal to N.
example: For N=13 and M=1, count=6 (numbers 1,10,11,12,13).'''


def count_occurrences(N, M):
    def count_in_number(number):
        count = 0
        while number > 0:
            if number % 10 == M:
                count += 1
            number //= 10
        return count
    
    total_count = 0
    for num in range(N + 1):
        total_count += count_in_number(num)
    return total_count

# Get inputs from the user
N = int(input("Enter the value of N (0 <= N <= 100): "))
M = int(input("Enter the value of M (0 <= M <= 9): "))

# Validate inputs
if not (0 <= N <= 100) or not (0 <= M <= 9):
    print("give valid input")
else:
    count = count_occurrences(N, M)
    print(f"The integer {M} occurs {count} times in all non-negative integers less than or equal to {N}.")


class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    # Addition - operator overloading
    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)
    
    # Addition - without operator overloading
    def add(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    # Subtraction - operator overloading
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)
    
    # Subtraction - without operator overloading
    def subtract(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    # Multiplication - operator overloading
    def __mul__(self, other):
        return Complex(self.real * other.real - self.imaginary * other.imaginary,
                       self.real * other.imaginary + self.imaginary * other.real)
    # Multiplication - without operator overloading
    def multiply(self, other):
        return Complex(self.real * other.real - self.imaginary * other.imaginary,
                       self.real * other.imaginary + self.imaginary * other.real)
    
    

    # Division - operator overloading
    def __truediv__(self, other):
        divisor = other.real ** 2 + other.imaginary ** 2
        real_part = (self.real * other.real + self.imaginary * other.imaginary) / divisor
        imaginary_part = (self.imaginary * other.real - self.real * other.imaginary) / divisor
        return Complex(real_part, imaginary_part)
    
    # Division - without operator overloading
    def divide(self, other):
        divisor = other.real ** 2 + other.imaginary ** 2
        real_part = (self.real * other.real + self.imaginary * other.imaginary) / divisor
        imaginary_part = (self.imaginary * other.real - self.real * other.imaginary) / divisor
        return Complex(real_part, imaginary_part)




    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {abs(self.imaginary)}i"



c1 = Complex(2, 3)
c2 = Complex(4, -5)


print( c1 + c2)
print(c1.add(c2))

print( c1 - c2)
print(c1.subtract(c2))


print( c1 * c2)
print( c1.multiply(c2))


print( c1 / c2)
print(c1.divide(c2))
