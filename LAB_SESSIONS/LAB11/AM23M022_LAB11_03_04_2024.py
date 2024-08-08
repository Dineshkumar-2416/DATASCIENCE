# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:24:42 2024

@author: mdine
"""
'''
1) (a ) Plot the sigmoid function. Print your interpretation on why this function is useful 
for a classification problem.

(b) Plot the log functions in the cost function individually. 
    Print your interpretation of the log functions

c) Using your own data for a single feature problem, and assuming linear regression problem, 
plot the cost function and the corresponding contours. 
Also, using cross entropy as the cost function, plot it as well as its contours.
'''



from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

#plotting y = x^2
z = np.arange(-8.0, 8.0, 0.01)
si = 1.0 / (1+np.e**(-z))

fig, ax = plt.subplots()
ax.plot(z, si)

ax.set(xlabel='z values', ylabel='sigma(z)',
       title='Sigmoid / logistic function')
ax.grid()


plt.show()

'''

Print your interpretation on why this function is useful 
for a classification problem.

 
The sigmoid function's output ranges from 0 to 1, 
which makes it suitable for representing probabilities. 
This property helps to find the output of the sigmoid function 
as the probability of a given input belonging to a certain 
class. Thus by this way, this function is useful 
for a classification problem.

'''

'''
(b) Plot the log functions in the cost function individually. 
    Print your interpretation of the log functions
'''


z = np.arange(0.01, 1.0, 0.01)
lo = -np.log(z)

fig, ax = plt.subplots()
ax.plot(z, lo)

ax.set(xlabel='values', ylabel='-log',
       title='-log function')
ax.grid()


plt.show()

z = np.arange(0.01, 1.0, 0.01)
lo = -np.log(1-z)

fig, ax = plt.subplots()
ax.plot(z, lo)

ax.set(xlabel='values', ylabel='-log(1-z)',
       title='-log(1-z) function')
ax.grid()


plt.show()

'''
c) Using your own data for a single feature problem, and assuming linear regression problem, 
plot the cost function and the corresponding contours. 
Also, using cross entropy as the cost function, plot it as well as its contours.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def gen_equ_gd(x,y):
    col= np.ones(x.shape[0])
    data= np.insert(x,0,col, axis=1)
    w= np.random.randn(data.shape[1])
    gradj=np.zeros(len(w))
    loss_var=[]
    for i in range(1000):
        h= data@w
        loss= (np.sum((h-y)**2))/(2*data.shape[1])
        loss_var.append(loss)
        for j in range(len(gradj)):
            gradj[j]= np.dot((h-y),data[:,j])/data.shape[0]
        w-=(0.01*gradj)
    return loss_var, w

# print(w)

data = pd.read_csv(r'E:\AM23M022_SEM2\DATASCIENCE_THEORY_AND_PRACTICE\Datascience_Submissions\LAB11\univariate_linear_regression.csv')

# Assuming the CSV has columns 'x' and 'y', and you want to use them for regression
x = data['x'].values.reshape(-1, 1)  # Reshape to make it a column vector
y = data['y'].values

# Call the function with loaded data
# print(gen_equ_gd(x, y))
loss_var,w = gen_equ_gd(x, y)
plt.plot(loss_var)
plt.title('Loss Function over Iterations')
plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.show()

# Plot the best fit line
plt.scatter(x, y, label='Data')
plt.plot(x, np.dot(np.insert(x, 0, np.ones(x.shape[0]), axis=1), w), color='red', label='Best Fit Line')
plt.title('Best Fit Line')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Plot the loss function as a surface
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
w0_vals = np.linspace(-20 ,20, 1000)
w1_vals = np.linspace(-20, 20, 1000)
w0, w1 = np.meshgrid(w0_vals, w1_vals)
# print(w0)
# print(w1)
J_vals = np.zeros_like(w0)
for i in range(len(w0_vals)):
    for j in range(len(w1_vals)):
        J_vals[i, j] = np.sum((x * w0[i, j] + w1[i, j] - y) ** 2) / (2 * x.shape[0])
ax.plot_surface(w0, w1, J_vals, cmap='viridis')
ax.set_xlabel('w0')
ax.set_ylabel('w1')
ax.set_zlabel('Loss')
ax.set_title('Loss Function Surface')
plt.show()

# Plot the loss function as a contour
plt.figure(figsize=(10, 6))
plt.contour(w1, w0, J_vals, levels= 100)
plt.xlabel('w0')
plt.ylabel('w1')
plt.title('Loss Function Contour')
plt.colorbar(label='Loss')
plt.show()

print("Weights for univariate:", w)


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def cross_entropy_cost_fn(x,y):
    col= np.ones(x.shape[0])
    data= np.insert(x,0,col, axis=1)
    w= np.random.randn(data.shape[1])
    gradj=np.zeros(len(w))
    loss_var=[]
    for i in range(1000):
        h= sigmoid(data@w)
        loss= np.sum(-y* np.log(h)-(1-y)*np.log(1-h))/data.shape[1]
        loss_var.append(loss)
        for j in range(len(gradj)):
            gradj[j]= np.dot((h-y),data[:,j])/data.shape[0]
        w-=(0.01*gradj)
    return loss_var, w




data = pd.read_csv(r'E:\AM23M022_SEM2\DATASCIENCE_THEORY_AND_PRACTICE\Datascience_Submissions\LAB11\univariate_linear_regression.csv')

# Assuming the CSV has columns 'x' and 'y', and you want to use them for regression
x = data['x'].values.reshape(-1, 1)  # Reshape to make it a column vector
y = np.random.randint(0,2,len(x))

# Call the function with loaded data
# print(gen_equ_gd(x, y))
loss_var,w = cross_entropy_cost_fn(x, y)
plt.plot(range(1000), loss_var)
plt.title('Loss Function over Iterations')
plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.show()

# # Plot the best fit line
# plt.scatter(x, y, label='Data')
# plt.plot(x, np.dot(np.insert(x, 0, np.ones(x.shape[0]), axis=1), w), color='red', label='Best Fit Line')
# plt.title('Best Fit Line')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()

# Plot the loss function as a surface
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
w0_vals = np.linspace(-2 ,2, 200)
w1_vals = np.linspace(-2, 2, 200)
w0, w1 = np.meshgrid(w0_vals, w1_vals)


J_vals = np.zeros_like(w0)
for i in range(len(w0_vals)):
    for j in range(len(w1_vals)):
        h= sigmoid(data @np.array([w0[i,j],w1[i,j]]))
        J_vals[i, j] =  np.sum(-y* np.log(h)-(1-y)*np.log(1-h))/data.shape[1]
ax.plot_surface(w1, w0, J_vals, cmap='viridis')
ax.set_xlabel('w0')
ax.set_ylabel('w1')
ax.set_zlabel('Loss')
ax.set_title('Loss Function Surface')
plt.show()

# Plot the loss function as a contour
plt.figure(figsize=(10, 6))
plt.contour(w0, w1, J_vals, levels= 150)
plt.xlabel('w0')
plt.ylabel('w1')
plt.title('Loss Function Contour')
plt.colorbar(label='Loss')
plt.show()

print("Weights for cross entropy:", w)

'''-------------'''
