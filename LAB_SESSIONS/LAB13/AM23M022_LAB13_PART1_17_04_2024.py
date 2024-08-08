''# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:16:33 2024
@author: mdine
"""

'''
1) Create the following data and write to a csv file:
    Generate 10 random points in each of the the following circles 
    (i) centre at (3,3) and radius 2, 
    (ii) centre at (7,7) and radius 2 
    (iii) centre at (11,11) and radius 
    2.  Plot the data as well.               

'''
    
    
    
import numpy as np
import matplotlib.pyplot as plt
import csv

# Define circle parameters
circle_params = [
    {"center": (3, 3), "radius": 2},
    {"center": (7, 7), "radius": 2},
    {"center": (11, 11), "radius": 2}
]

# Generate random points in each circle
num_points = 10
points = []

for circle in circle_params:
    center = circle["center"]
    radius = circle["radius"]
    for _ in range(num_points):
        theta = np.random.uniform(0, 2*np.pi)
        r = np.sqrt(np.random.uniform(0, radius**2))
        x = center[0] + r * np.cos(theta)
        y = center[1] + r * np.sin(theta)
        points.append((x, y))

# Plot the initial random data
for circle in circle_params:
    center = circle["center"]
    radius = circle["radius"]
    plt.scatter(center[0], center[1], color='red', marker='o')
    circle_plot = plt.Circle(center, radius, color='blue', fill=False)
    plt.gca().add_artist(circle_plot)

x_values = [point[0] for point in points]
y_values = [point[1] for point in points]
plt.scatter(x_values, y_values, color='black', marker='x')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Random Points in Circles')
plt.axis('equal')
plt.grid(True)
plt.show()

# Write points to CSV file
with open('random_points.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['X', 'Y'])
    for point in points:
        csv_writer.writerow(point)
        
'''
        2)  Implement K - means clustering algorithm (with out using sklearn library) and for the above data, 
            show the change in the centroid as well as the class assignments. 
            Also, plot the cost function for K varying from 1 to 5. 
            Show that the value of K matches with the intuition from the data. 
            Plot the K-classes for the final K-value.     '''
            
            
            
            

# Load the data from the CSV file
data = np.loadtxt('random_points.csv', delimiter=',', skiprows=1)

class Kmeans:
    def __init__(self, data, K):
        self.data = data
        self.K = K
    
    def fit(self, max_iterations):
        # Initialize centroids randomly
        self.centroids = self.data[np.random.choice(self.data.shape[0], self.K, replace=False)]
        self.labels = None
        
        # Lists to store centroid updates and costs
        self.centroid_updates = [self.centroids]
        self.costs = []
        
        # Loop until centroids no longer change or max_iterations reached
        for _ in range(max_iterations):
            # Assign each point to the nearest centroid
            distances = 1/len(self.centroids)*np.linalg.norm(self.data[:, np.newaxis] - self.centroids, axis=2)
            self.labels = np.argmin(distances, axis=1)
            
            # Update centroids
            new_centroids = np.array([self.data[self.labels == k].mean(axis=0) for k in range(self.K)])
            
            # Calculate total cost
            cost = np.sum(np.min(distances, axis=1))
            self.costs.append(cost)
            
            # Check if centroids have changed
            if np.allclose(new_centroids, self.centroids):
                break
            
            # Update centroids
            self.centroids = new_centroids
            
            # Store centroid updates
            self.centroid_updates.append(self.centroids)
    
    def predict(self):
        return self.labels, self.centroids

# Initialize an empty array to store costs for different K values
costs = np.array([])

# Define range of K values
K_values = range(1, 6)

# Iterate over different values of K
for K in K_values:
    # Perform KMeans clustering
    kmeans = Kmeans(data, K)
    kmeans.fit(100)  # Assuming max_iterations is 100
    
    # Calculate cost (within-cluster norm)
    distances = np.linalg.norm(data[:, np.newaxis] - kmeans.centroids, axis=2)
    cost = np.sum(np.min(distances, axis=1))
    
    # Append cost to the array
    costs = np.append(costs, cost)
    
    # Plot centroid updates for each iteration
    for i, centroid_update in enumerate(kmeans.centroid_updates):
        plt.figure(figsize=(8, 6))
        plt.scatter(data[:, 0], data[:, 1], c=kmeans.labels, cmap='viridis', marker='x', alpha=0.7)
        plt.scatter(centroid_update[:, 0], centroid_update[:, 1], marker='o', s=200, c='red', label='Centroids')
        plt.title(f'K-Means Clustering with K={K} - Iteration {i+1}')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.show()

# Plot the costs against the number of clusters K
plt.plot(K_values, costs)
plt.xlabel('Number of Clusters')
plt.ylabel('Cost')
plt.title('Cost Function for Different Values of K')
plt.xticks(K_values)
plt.grid(True)
plt.show()

''' Show that the value of K matches with the intuition from the data. 
 Plot the K-classes for the final K-value. 
 
 Solution : the data we generated is 3 centres and 3 radius and obviously the optimal value of k will be 3 as we can see from
 the data plot. 
 
 plot of k =3 after several iteration can be seen from the plot as k  =3 seems to the optimal number of clusters
 The elbow method also show k =3 as the  optimal one from the number of clusters vs cost function plot'''