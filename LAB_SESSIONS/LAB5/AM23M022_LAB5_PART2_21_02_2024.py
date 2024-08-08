# -*- coding: utf-8 -*-
"""
Created on Feb 22 22:33:59 2024

@author: mdine
"""
'''
 5. WAP to implement a class called "Bank_Account" representing a person's bank account.
The class should have the following attributes: account_holder_name (str), account_number(int), address (str) and balance (float).
The class should have methods to implement the following:
    deposit - Deposits a given amount into the account
    withdraw - Withdraws a given amount from the account
    check_balance - To get the current balance
    update_details - To update the name and address from the user and displays a message indicating successful update
    display_details - To display the details of the account."""
'''

class Bank_Account:
    def __init__(self, account_holder_name, account_number, address, balance):
        self.account_holder_name = str(account_holder_name)
        self.account_number = int(account_number)
        self.address = str(address)
        self.balance = float(balance)
    
    def deposit_amount(self, amount):
        self.balance += amount
        print(f"Deposit successful. Balance is now {self.balance}")
                
        
    def withdraw_amount(self, withdrawal_amount):
        if withdrawal_amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= withdrawal_amount
            return f"Withdrawal successful. Remaining balance is {self.balance}"
            
    def check_balance(self):
        print(f"Your current balance is: {self.balance}")
    
    def update_details(self, new_name, new_address):
        self.account_holder_name = new_name
        self.address = new_address
        print("New name and address details updated successfully.")
        print("\n")
        
    def display_details(self):
        print("Account Holder Name:", self.account_holder_name)
        print("Account Number:", self.account_number)
        print("Address:", self.address)
        print("Balance:", self.balance)

bank_acc = Bank_Account("DINESH", 2416, " pallikaranai", 3025)   
bank_acc.display_details()
print("\n")

result = bank_acc.withdraw_amount(1000) 
print(result)  
print("\n")

bank_acc.update_details("KAVI PR", "Coimbatore")
bank_acc.display_details() 

bank_acc.check_balance()  

bank_acc.deposit_amount(20000)


"""7. Create a Python class named Time that represents a moment of time. The class should have attributes hour, minute, and second. Include the following features:
    A constructor that initializes hour, minute, and second, with validation to ensure each attribute is within its correct range (hours: 0-23, minutes: 0-59, seconds: 0-59).
    A __str__() method that returns the time in a format hh:mm:ss.
    Methods set_time(hour, minute, second) and get_time() to update and access the time, respectively.
    An add_seconds(seconds) method that adds a given number of seconds to the current time object, adjusting the hour, minute, and second attributes accordingly.
"""

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.set_time(hour, minute, second)

    def set_time(self, hour, minute, second):
        if 0 <= hour < 24:
            self.hour = hour
        else:
            raise ValueError("Hour must be between 0 and 23")
        if 0 <= minute < 60:
            self.minute = minute
        else:
            raise ValueError("Minute must be between 0 and 59")
        if 0 <= second < 60:
            self.second = second
        else:
            return ValueError("Second must be between 0 and 59")

    def get_time(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def add_seconds(self, seconds):
        total_seconds = self.hour * 3600 + self.minute * 60 + self.second + seconds
        self.hour = total_seconds // 3600 % 24
        self.minute = total_seconds // 60 % 60
        self.second = total_seconds % 60

    def __str__(self):
        return self.get_time()

# Example usage without try-except block
t = Time(23, 59, 45)
print("Initial time:", t)
t.add_seconds(20)
print("After adding 20 seconds:", t)

t.set_time(8, 30, 15)
print("New time:", t)



"""8.  Create a class named Geometry that provides static methods for various geometric calculations, such as area and perimeter, for different shapes (circle, rectangle, square). Include:
Static methods like circle_area(radius), rectangle_area(length, width), and square_area(side).
Static methods for perimeter calculations for the above shapes.
Ensure that methods check for valid inputs (e.g., positive numbers).
"""    
import math

class Geometry:
    @staticmethod
    def circle_area(radius):
        if radius <= 0:
            return "Radius must be a positive number"
        return math.pi * radius**2

    @staticmethod
    def circle_perimeter(radius):
        if radius <= 0:
            return "Radius must be a positive number"
        return 2 * math.pi * radius

    @staticmethod
    def rectangle_area(length, width):
        if length <= 0 or width <= 0:
            return "Length and width must be positive numbers"
        return length * width

    @staticmethod
    def rectangle_perimeter(length, width):
        if length <= 0 or width <= 0:
            return "Length and width must be positive numbers"
        return 2 * (length + width)

    @staticmethod
    def square_area(side):
        if side <= 0:
            return "Side length must be a positive number"
        return side**2

    @staticmethod
    def square_perimeter(side):
        if side <= 0:
            return "Side length must be a positive number"
        return 4 * side


# Example usage:
print("Circle area:", Geometry.circle_area(5))
print("Circle perimeter:", Geometry.circle_perimeter(5))
print("Rectangle area:", Geometry.rectangle_area(4, 6))
print("Rectangle perimeter:", Geometry.rectangle_perimeter(4, 6))
print("Square area:", Geometry.square_area(4))
print("Square perimeter:", Geometry.square_perimeter(4))


'''
"""6.  Define a Matrix class of dimensions m X n (the values for m and n can be taken as input).
 Demonstrate matrix addition, subtraction, multiplication, element-by-element multiplication, 
scalar multiplication (use map here). Use operator overloading wherever possible.
 (Hint: In the constructor, use 'random' and create list of list using list comprehension. 
  In the arguments of constructor, send the number of rows and columns)
Ensure that your implementation follows best practices for class design and encapsulation in Python. 
Comment your code to explain the functionality of each method."""

'''

import random

class MatrixOperations:
    def __init__(self, rows, columns): 
        self.rows = rows
        self.columns = columns
        self.data = [[random.randint(1, 10) for _ in range(columns)] for _ in range(rows)]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def matrix_addition(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            print("Matrices must have the same dimensions for addition.")
            return None
        result = MatrixOperations(self.rows, self.columns)
        result.data = [[self.data[i][j] + other.data[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return result

    def matrix_subtraction(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            print("Matrices must have the same dimensions for subtraction.")
            return None
        result = MatrixOperations(self.rows, self.columns)
        result.data = [[self.data[i][j] - other.data[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return result

    def matrix_multiplication(self, other):
        if self.columns != other.rows:
            print("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
            return None
        result = MatrixOperations(self.rows, other.columns)
        result.data = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.columns)) for j in range(other.columns)] for i in range(self.rows)]
        return result

    def elementwise_multiply(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            print("Matrices must have the same dimensions for element-wise multiplication.")
            return None
        result = MatrixOperations(self.rows, self.columns)
        result.data = [[self.data[i][j] * other.data[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return result

    def scalar_multiplication(self, scalar):
        result = MatrixOperations(self.rows, self.columns)
        result.data = list(map(lambda row: list(map(lambda x: scalar * x, row)), self.data))
        return result



m1 = MatrixOperations(2, 3)
m2 = MatrixOperations(2, 3)
print("Matrix 1:")
print(m1)
print("Matrix 2:")
print(m2)

print("Matrix Addition:")
print(m1.matrix_addition(m2))

print("Matrix Subtraction:")
print(m1.matrix_subtraction(m2))

print("Matrix Multiplication:")
m3 = MatrixOperations(3, 2)
print(m1.matrix_multiplication(m3))

print("Element-wise Multiplication:")
print(m1.elementwise_multiply(m2))

print("Scalar Multiplication:")
print(m1.scalar_multiplication(2))


