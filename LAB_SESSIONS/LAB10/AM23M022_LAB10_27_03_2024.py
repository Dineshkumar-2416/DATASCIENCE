# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 14:36:19 2024

@author: mdine
"""
'''
1. Implement the generalized equation for finding the gradient of m-samples, each having n-features. 
Also, implement the gradient descent approach assuming a constant learning rate
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def eqn_grad_msamples(x,y):
    col = np.ones(x.shape[0])
    data = np.insert(x, 0, col, axis=1)
    w = np.random.randn(data.shape[1])
    gradj = np.zeros(len(w))
    loss_var = []
    for i in range(4000):
        h = data@w
        loss=(np.sum((h-y)**2))/(2*data.shape[1])
        loss_var.append(loss)
        for j in range(len(gradj)):
            gradj[j] = np.dot((h-y),data[:,j])/data.shape[0]
        w = w-(0.01*gradj)
        
    return loss_var,w


'''
2) Using the code developed for problem 1, do the linear regression for the univariate problem 
    using the attached data file univariate_linear_regression.csv. 
    Plot the cost function (both as surface as well as contour) as well as the best fit line. 
'''            
  
# Read the CSV file
data = pd.read_csv('univariate_linear_regression.csv')

# Print the first few rows of the data to check if it's read correctly
print(data.head())

# Access specific columns if needed
X = data['x'].values.reshape(-1, 1)  # Convert to NumPy array and then reshape
y = data['y']  # Assuming 'y' is the name of the column containing output variable

# Call the function to compute the cost function and optimized weights
cost_fn, weights = eqn_grad_msamples(X, y)

# Plot the cost function
plt.plot(cost_fn)
plt.xlabel('Iteration')
plt.ylabel('Cost')
plt.title('Cost Function')
plt.show()

# Define a range of parameter values for w0 and w1
w0_range = np.linspace(-20, 20, 100)
w1_range = np.linspace(-20, 20, 100)
W0, W1 = np.meshgrid(w0_range, w1_range)

# Compute the cost function for each combination of parameters
Z = np.zeros_like(W0)
for i in range(len(w0_range)):
    for j in range(len(w1_range)):
        h = W0[i, j] + W1[i, j] * X.flatten()
        Z[i, j] = np.sum((h - y) ** 2) / (2 * len(X))
        
# Plot the surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(W0, W1, Z)
ax.set_xlabel('Intercept (w0)')
ax.set_ylabel('Slope (w1)')
ax.set_zlabel('Cost')
ax.set_title('Surface Plot of Cost Function')

# Plot the loss function as a contour
plt.figure(figsize=(10, 6))
plt.contour(W0, W1, Z, levels= 100)
plt.xlabel('w0')
plt.ylabel('w1')
plt.title('Loss Function Contour')
plt.colorbar(label='Loss')
plt.show()


# Plot the best fit line
plt.scatter(X, y, label='Data')
plt.plot(X, np.dot(np.insert(X, 0, np.ones(X.shape[0]), axis=1), weights), color='red', label='Best Fit Line')
plt.title('Best Fit Line')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

'''
3) Using the code developed for problem 1, 
    do the linear regression for the multivariate problem using the attached data file heart.data.csv. 
    Plot the best fit plane for the given data. Can you also interpret the result 
    (taking one independent variable at a time)? 
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file
data1 = pd.read_csv('heart.data.csv')
data = (data1 - data1.mean()) / data1.std()

# Extract independent variables (features) X1, X2, ... and the dependent variable (target) y
X = data[['biking', 'smoking']].values
y = data['heart.disease'].values

def multivariate_linear_regression(X, y):
    col = np.ones(X.shape[0])
    data = np.insert(X, 0, col, axis=1)
    w = np.random.randn(data.shape[1])
    gradj = np.zeros(len(w))
    loss_var = []
    for i in range(40000):  # Increase number of iterations
        h = data @ w
        loss = (np.sum((h - y) ** 2)) / (2 * data.shape[0])  # Update the denominator here
        loss_var.append(loss)
        for j in range(len(gradj)):
            gradj[j] = np.dot((h - y), data[:, j]) / data.shape[0]
        w -= (0.001 * gradj)  # Adjust learning rate
    return loss_var, w

# Compute weights for multivariate linear regression
loss_var, w = multivariate_linear_regression(X, y)
print("Weights:", w)

# Generate grid points for X1 and X2 to create the mesh grid
biking_range = np.linspace(min(X[:, 0]), max(X[:, 0]), 10)
smoking_range = np.linspace(min(X[:, 1]), max(X[:, 1]), 10)
biking_mesh, smoking_mesh = np.meshgrid(biking_range, smoking_range)

# Define a function to compute z-values (predicted values) for the plane
def compute_z_values(biking_mesh, smoking_mesh, w):
    col = np.ones(biking_mesh.shape)
    data = np.stack((col, biking_mesh, smoking_mesh), axis=-1)
    z_values = np.sum(data * w, axis=-1)
    return z_values

# Compute z-values for the plane using the weights obtained from linear regression
z_values = compute_z_values(biking_mesh, smoking_mesh, w)

# Plot the data points and the best fit plane
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the data points
ax.scatter(X[:, 0], X[:, 1], y, color='blue', label='Data Points')

# Plot the best fit plane
ax.plot_surface(biking_mesh, smoking_mesh, z_values, alpha=0.5, cmap='viridis', label='Best Fit Plane')

# Set labels and title
ax.set_xlabel('Biking')
ax.set_ylabel('Smoking')
ax.set_zlabel('Heart Disease')
ax.set_title('Best Fit Plane for Multivariate Linear Regression')

# Add a legend
ax.legend()

# Show plot
plt.show()

print("Weights:", w)

# Compute correlation coefficients
correlation_smoking = data['smoking'].corr(data['heart.disease'])
correlation_biking = data['biking'].corr(data['heart.disease'])

print("Correlation between smoking and heart disease:", correlation_smoking)
print("Correlation between biking and heart disease:", correlation_biking)

# Plot the scatter plots
plt.figure(figsize=(10, 6))

# Scatter plot for smoking vs heart disease
plt.subplot(1, 2, 1)
plt.scatter(X[:, 1], y, color='blue')
plt.xlabel('Smoking')
plt.ylabel('Heart Disease')
plt.title(f'Correlation: {correlation_smoking:.2f}')

# Scatter plot for biking vs heart disease
plt.subplot(1, 2, 2)
plt.scatter(X[:, 0], y, color='red')
plt.xlabel('Biking')
plt.ylabel('Heart Disease')
plt.title(f'Correlation: {correlation_biking:.2f}')

plt.tight_layout()
plt.show()
