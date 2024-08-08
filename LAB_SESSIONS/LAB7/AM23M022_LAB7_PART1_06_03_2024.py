# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:45:50 2024

@author: mdine
"""
'''

1. Write a program that takes coefficients A, B, C, D, and E 
as inputs representing a 4th degree polynomial in the form 
Ax^4 + Bx^3 + Cx^2 + Dx + E.
 Calculate the values of this polynomial for x 
 in the range from -100 to 100, with constant discrete intervals.

Store the resulting x and y values as a NumPy array, 
where x represents the input values, and y represents 
the corresponding output values of the polynomial. 
Finally, use Matplotlib to plot the graph using 
the generated NumPy array.
'''



import numpy as np
import matplotlib.pyplot as plt

def calculate_polynomial(A, B, C, D, E, x_values):
    
    y_values = A * x_values**4 + B * x_values**3 + C * x_values**2 + D * x_values + E
    return y_values

def main():
    # Coefficients of the polynomial
    A = float(input("Enter coefficient A: "))
    B = float(input("Enter coefficient B: "))
    C = float(input("Enter coefficient C: "))
    D = float(input("Enter coefficient D: "))
    E = float(input("Enter coefficient E: "))

    # Generate x values from -100 to 100 with a constant discrete interval
    x_values = np.linspace(-100, 100, 1000)

    # Calculate y values for the polynomial
    y_values = calculate_polynomial(A, B, C, D, E, x_values)

    # Create a NumPy array for x and y values
    data = np.array([x_values, y_values])

    # Transpose the data array to have x and y values in separate rows
    data = data.T

    # Plot the graph
    plt.plot(data[:,0], data[:,1])
    plt.title('Plot of the 4th degree polynomial')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()

'''
2. Suppose you have a dictionary containing information about monthly sales for different products over a period of time. The dictionary has the following structure.

sales_data = {

    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'C'],

    'Month': ['Jan', 'Jan', 'Feb', 'Feb', 'Mar', 'Mar', 'Apr', 'Apr', 'Apr'],

    'Sales': [100, 150, 200, 120, 180, 220, 90, 110, 130]

}

Write a Python script to convert this dictionary into a pandas DataFrame, calculate the total sales for each product over the entire period, and then create a bar plot using matplotlib to visualize the total sales for each product.
'''



import pandas as pd
import matplotlib.pyplot as plt

# Define the sales data dictionary
sales_data = {
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'C'],
    'Month': ['Jan', 'Jan', 'Feb', 'Feb', 'Mar', 'Mar', 'Apr', 'Apr', 'Apr'],
    'Sales': [100, 150, 200, 120, 180, 220, 90, 110, 130]
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(sales_data)

# Calculate the total sales for each product over the entire period
total_sales = df.groupby('Product')['Sales'].sum().reset_index()
print(total_sales)

# Plot the total sales for each product
plt.bar(total_sales['Product'], total_sales['Sales'])
plt.title('Total Sales for Each Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()

'''
3. Create visualizations for the following mathematical functions using Matplotlib:

Plot the following single-variable functions over the range 

[−10,10], and include a title and labels for the axes:

(1) y = cos(x)

(2) y = e^x

(3) y = log(x), where x>0
'''


import numpy as np
import matplotlib.pyplot as plt

# Define the range
x = np.linspace(-10, 10, 700)

# y = cos(x)
y1 = np.cos(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y1, label='y = cos(x)', color='blue')
plt.title('Plot of y = cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# y = e^x
y2 = np.exp(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y2, label='y = e^x', color='red')
plt.title('Plot of y = e^x')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

#  y = log(x), where x > 0
x_positive = x[x > 0]  # Consider only positive x values for log function
y3 = np.log(x_positive)

plt.figure(figsize=(8, 6))
plt.plot(x_positive, y3, label='y = log(x)', color='green')
plt.title('Plot of y = log(x), where x > 0')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()


'''
Generate surface plots for these multi-variable functions over the range 

x=[−10,10] and y=[−10,10] , ensuring to add a title and labels for all axes:

(1) z = cos(sqrt(x^2+y^2)

(2) z = e^(-(x^2+y^2))

(3) z =  log(x^2+y^2) where x^2+y^2>0
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the range for x and y
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

# Create a meshgrid for x and y
X, Y = np.meshgrid(x, y)

#  z = cos(sqrt(x^2+y^2))
Z1 = np.cos(np.sqrt(X**2 + Y**2))

fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(111, projection='3d')
ax1.plot_surface(X, Y, Z1)
ax1.set_title('Surface Plot of z = cos(sqrt(x^2 + y^2))')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
plt.show()

# z = e^(-(x^2+y^2))
Z2 = np.exp(-(X**2 + Y**2))

fig = plt.figure(figsize=(10, 8))
ax2 = fig.add_subplot(111, projection='3d')
ax2.plot_surface(X, Y, Z2)
ax2.set_title('Surface Plot of z = e^(-(x^2 + y^2))')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
plt.show()

# z = log(x^2+y^2), where x^2+y^2 > 0
R = np.sqrt(X**2 + Y**2)
Z3 = np.log(R)

fig = plt.figure(figsize=(10, 8))
ax3 = fig.add_subplot(111, projection='3d')
ax3.plot_surface(X, Y, Z3)
ax3.set_title('Surface Plot of z = log(x^2 + y^2), where x^2 + y^2 > 0')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_zlabel('z')
plt.show()

'''
4. For the function J(w) = w^2 + (54/w), implement the bracketing method (choose your own a, b, n).'''

import numpy as np
import matplotlib.pyplot as plt

# Define the function
def J(w):
    return w**2 + (54 / w)

# Generate values for w
w_values = np.linspace(-10, 10, 400)  # adjust the range as needed

# Calculate corresponding values for J(w)
J_values = J(w_values)

# Plot the function
plt.figure(figsize=(8, 6))
plt.plot(w_values, J_values, label='$J(w) = w^2 + \\frac{54}{w}$', color='blue')
plt.title('Plot of $J(w)$')
plt.xlabel('w')
plt.ylabel('J(w)')
plt.grid(True)
plt.legend()
plt.show()

def J(w):
 
  return w**2 + (54/w)

def bracketing_method(a, b, n):
  
  # Check if function is continuous and monotonic over the interval
  # if not (J(a) * J(b) < 0):
  #   print("Function not continuous or monotonic in the given interval.")
  #   return None

  # Initialize variables
  fa = J(a)
  fb = J(b)
  for i in range(n):
    # Calculate midpoint
    c = (a + b) / 2
    fc = J(c)

    # Update interval based on function values
    if fa * fc < 0:
      b = c
      fb = fc
    else:
      a = c
      fa = fc

  # Minimum value is assumed to be the midpoint of the final interval
  return (a + b) / 2

# Define parameters
a = 1
b = 10
n = 10

# Find minimum using bracketing method
minimum = bracketing_method(a, b, n)

# Print the result
if minimum:
  print(f"Minimum value of J(w) found using bracketing method: {minimum:.4f}")
else:
  print("Minimum value not found.")


