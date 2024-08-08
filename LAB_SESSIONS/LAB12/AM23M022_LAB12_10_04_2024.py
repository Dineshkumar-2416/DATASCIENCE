# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 15:37:23 2024

@author: mdine
"""
'''
Q.1 Support Vector Machine:

Data and other details are available at 

https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html

Use the weblink and reproduce the result for SVM.

Implement SVM to classify the type of iris flower based on its sepal length and width using the iris dataset? 
Also try to use the scikit-learn digits dataset and an SVM to classify handwritten digits? 
For both datasets, provide a step-by-step code, including:  

Loading the dataset 
Visualizing the data 
Splitting the data into training and testing sets 
Initializing and training the SVM model 
Testing the model 

'''


import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

# Load the Iris dataset
iris = datasets.load_iris()

# Print the entire dataset
print("Dataset:")
print("Features:\n", iris.data)
print("Target:\n", iris.target)
print("Feature Names:", iris.feature_names)
print("Target Names:", iris.target_names)

# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load Iris dataset
iris = datasets.load_iris()
X_iris = iris.data[:, :2]  # Using only first two features (sepal length and width)
y_iris = iris.target

# Load Digits dataset
digits = datasets.load_digits()
X_digits = digits.data
y_digits = digits.target

# Function to visualize the data
def visualize_data(X, y, dataset_name):
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1, edgecolor='k')
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')
    plt.title(f'{dataset_name} Dataset')
    plt.show()

# Visualize Iris dataset
visualize_data(X_iris, y_iris, 'Iris')

# Visualize Digits dataset
def visualize_digits(X, y, dataset_name):
    plt.figure(figsize=(12, 6))
    for i in range(10):
        plt.subplot(2, 5, i + 1)
        plt.imshow(X[y == i][0].reshape(8, 8), cmap='binary', interpolation='nearest')
        plt.title(f'Digit: {i}')
        plt.axis('off')
    plt.suptitle(f'Sample Digits from {dataset_name} Dataset', fontsize=16)
    plt.show()

visualize_digits(X_digits, y_digits, 'Digits')



# Splitting the data into training and testing sets
X_train_iris, X_test_iris, y_train_iris, y_test_iris = train_test_split(X_iris, y_iris, test_size=0.2, random_state=42)
X_train_digits, X_test_digits, y_train_digits, y_test_digits = train_test_split(X_digits, y_digits, test_size=0.2, random_state=42)

# Standardizing the features
scaler = StandardScaler()
X_train_iris = scaler.fit_transform(X_train_iris)
X_test_iris = scaler.transform(X_test_iris)
X_train_digits = scaler.fit_transform(X_train_digits)
X_test_digits = scaler.transform(X_test_digits)

# Initializing and training the SVM model for Iris dataset
svm_iris = SVC(kernel='linear', random_state=42)
svm_iris.fit(X_train_iris, y_train_iris)

# Initializing and training the SVM model for Digits dataset
svm_digits = SVC(kernel='rbf', random_state=42)
svm_digits.fit(X_train_digits, y_train_digits)

# Testing the model for Iris dataset
y_pred_iris = svm_iris.predict(X_test_iris)
accuracy_iris = accuracy_score(y_test_iris, y_pred_iris)
print("Accuracy for Iris dataset:", accuracy_iris)
print("Confusion Matrix for Iris dataset:")
print(confusion_matrix(y_test_iris, y_pred_iris))
print("Classification Report for Iris dataset:")
print(classification_report(y_test_iris, y_pred_iris))

# Testing the model for Digits dataset
y_pred_digits = svm_digits.predict(X_test_digits)
accuracy_digits = accuracy_score(y_test_digits, y_pred_digits)
print("\nAccuracy for Digits dataset:", accuracy_digits)
print("Confusion Matrix for Digits dataset:")
print(confusion_matrix(y_test_digits, y_pred_digits))
print("Classification Report for Digits dataset:")
print(classification_report(y_test_digits, y_pred_digits))



'''
Q. 2 Principal Component Analysis:

To do PCA, use the Eigen decomposition available in numpy. The dataset can be obtained from https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_3d.html#sphx-glr-auto-examples-decomposition-plot-pca-3d-py. 
DO NOT USE the code available for PCA in the same link (as mentioned above, use numpy's Eigen decomposition). 
Compare your results with the one available in the link (here, you are free to use the code available in the link to generate any numbers for comparison). 
Are you getting the same result?'''


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Importing this module to enable 3D plotting
from sklearn import datasets
from sklearn.preprocessing import StandardScaler

# Load the Iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

# Standardize the features
scaler = StandardScaler()
X_standardized = scaler.fit_transform(X)

# Calculate the covariance matrix
cov_matrix = np.cov(X_standardized, rowvar=False)

# Perform eigen decomposition
eigen_values, eigen_vectors = np.linalg.eig(cov_matrix)

# Sort eigenvalues and eigenvectors in descending order
sorted_indices = np.argsort(eigen_values)[::-1]
eigen_values_sorted = eigen_values[sorted_indices]
eigen_vectors_sorted = eigen_vectors[:, sorted_indices]

# Define the range of n_components
n_components_range = [1, 2, 3]

# Visualize the dataset for different n_components
fig, axes = plt.subplots(1, len(n_components_range), figsize=(15, 5), subplot_kw={'projection': '3d'})

for i, n_components in enumerate(n_components_range):
    # Select the top n_components principal components
    projection_matrix = eigen_vectors_sorted[:, :n_components]
    X_pca = np.dot(X_standardized, projection_matrix)

    # Scatter plot for each class
    for j in np.unique(y):
        if n_components == 1:
            axes[i].scatter(X_pca[y == j, 0], np.zeros_like(X_pca[y == j, 0]), np.zeros_like(X_pca[y == j, 0]), label=f'Class {j}')
        elif n_components == 2:
            axes[i].scatter(X_pca[y == j, 0], X_pca[y == j, 1], np.zeros_like(X_pca[y == j, 1]), label=f'Class {j}')
        else:
            axes[i].scatter(X_pca[y == j, 0], X_pca[y == j, 1], X_pca[y == j, 2], label=f'Class {j}')

    axes[i].set_xlabel('Principal Component 1')
    if n_components > 1:
        axes[i].set_ylabel('Principal Component 2')
    if n_components == 3:
        axes[i].set_zlabel('Principal Component 3')
    axes[i].set_title(f'PCA with {n_components} components')
    axes[i].legend()

    # Print eigenvalues, eigenvectors, and explained variance
    print(f"For n_components = {n_components}:")
    print("Eigenvalues:", eigen_values_sorted[:n_components])
    print("Eigenvectors:\n", eigen_vectors_sorted[:, :n_components])
    explained_variance_ratio = eigen_values_sorted[:n_components] / np.sum(eigen_values_sorted)
    print("Explained Variance Ratio:", explained_variance_ratio)

plt.show()

'''
Compare your results with the one available in the link (here, you are free to use the code available in the link to generate any numbers for comparison). 
Are you getting the same result?



For n_components = 1:
Eigenvalues: [2.93808505]
Eigenvectors:
 [[ 0.52106591]
 [-0.26934744]
 [ 0.5804131 ]
 [ 0.56485654]]
Explained Variance Ratio: [0.72962445]
For n_components = 2:
Eigenvalues: [2.93808505 0.9201649 ]
Eigenvectors:
 [[ 0.52106591 -0.37741762]
 [-0.26934744 -0.92329566]
 [ 0.5804131  -0.02449161]
 [ 0.56485654 -0.06694199]]
Explained Variance Ratio: [0.72962445 0.22850762]
For n_components = 3:
Eigenvalues: [2.93808505 0.9201649  0.14774182]
Eigenvectors:
 [[ 0.52106591 -0.37741762 -0.71956635]
 [-0.26934744 -0.92329566  0.24438178]
 [ 0.5804131  -0.02449161  0.14212637]
 [ 0.56485654 -0.06694199  0.63427274]]
 Explained Variance Ratio: [0.72962445 0.22850762 0.03668922]
 
 For n_components = 2:
Explained Variance Ratio (PCA : EIGEN DECOMPOSITION):
    [0.72962445 0.22850762] 
explained variance ratio (first two components) other method n=2 : 
        [0.92461872 0.05306648] 
explained variance ratio (first two components) using LDA
: [0.9912126 0.0087874]
       
Results are different
    


=======================================================
Comparison of LDA and PCA 2D projection of Iris dataset
=======================================================

The Iris dataset represents 3 kind of Iris flowers (Setosa, Versicolour
and Virginica) with 4 attributes: sepal length, sepal width, petal length
and petal width.

Principal Component Analysis (PCA) applied to this data identifies the
combination of attributes (principal components, or directions in the
feature space) that account for the most variance in the data. Here we
plot the different samples on the 2 first principal components.

Linear Discriminant Analysis (LDA) tries to identify attributes that
account for the most variance *between classes*. In particular,
LDA, in contrast to PCA, is a supervised method, using known class labels.
'''



import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

iris = datasets.load_iris()

X = iris.data
y = iris.target
target_names = iris.target_names

pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)

lda = LinearDiscriminantAnalysis(n_components=2)
X_r2 = lda.fit(X, y).transform(X)

# Percentage of variance explained for each components
print(
    "explained variance ratio (first two components): %s"
    % str(pca.explained_variance_ratio_)
)

plt.figure()
colors = ["navy", "turquoise", "darkorange"]
lw = 2

for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(
        X_r[y == i, 0], X_r[y == i, 1], color=color, alpha=0.8, lw=lw, label=target_name
    )
plt.legend(loc="best", shadow=False, scatterpoints=1)
plt.title("PCA of IRIS dataset")

plt.figure()
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(
        X_r2[y == i, 0], X_r2[y == i, 1], alpha=0.8, color=color, label=target_name
    )
plt.legend(loc="best", shadow=False, scatterpoints=1)
plt.title("LDA of IRIS dataset")

plt.show()
# Percentage of variance explained for each components
print(
    "explained variance ratio (first two components): %s"
    % str(lda.explained_variance_ratio_)
)
