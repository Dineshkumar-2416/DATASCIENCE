# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:34:24 2024

@author: mdine
"""

'''
Implement the forward propagation for a two hidden layer network for m-samples, n-features 
as we discussed in class. Initialize the weights randomly. 
Use the data from the previous labs like logistic regression. 
You can choose the number of neurons in the hidden layer and use sigmoid activation function.
Report the evaluation metrics for the network.  
Also use other non-linear activation functions like ReLU and Tanh. 
Report the loss using both MSE and Cross Entropy'''


import numpy as np
import pandas as pd

data = pd.read_csv(r"E:\AM23M022_SEM2\DATASCIENCE_THEORY_AND_PRACTICE\Datascience_Submissions\LAB14\random_points.csv")

X_data = data.iloc[:, :2].values
y_data = data.iloc[:, 2].values

def activation_function(s, activation_type):
    if activation_type == 'sigmoid':
        return 1 / (1 + np.exp(-s))
    elif activation_type == 'tanh':
        return np.tanh(s)
    elif activation_type == 'relu':
        return np.maximum(0, s)

class NeuralNetwork:
    def __init__(self, hidden_activation_type='sigmoid'):
        self.weights1 = np.random.random((2, 4))  
        self.biases1 = np.random.random(4)  
        self.weights2 = np.random.random((4, 1))  
        self.biases2 = np.random.random(1)  
        
        self.hidden_activation_type = hidden_activation_type
        
    def forward(self, X):
        # Forward pass through layer 1
        z1 = np.dot(X, self.weights1) + self.biases1
        a1 = activation_function(z1, self.hidden_activation_type)
        
        # Forward pass through layer 2
        z2 = np.dot(a1, self.weights2) + self.biases2
        a2 = activation_function(z2, 'sigmoid')
        
        return a2
    
    def predict(self, X):
        return np.round(self.forward(X))

hidden_activation_type = 'sigmoid' 
nn_model = NeuralNetwork(hidden_activation_type=hidden_activation_type)

# Define the train_test_split function
def custom_train_test_split(X, y, test_size=0.3, random_state=None):
    if random_state:
        np.random.seed(random_state)
    indices = np.random.permutation(X.shape[0])
    test_size = int(X.shape[0] * test_size)
    test_indices = indices[:test_size]
    train_indices = indices[test_size:]
    return X[train_indices], X[test_indices], y[train_indices], y[test_indices]

# Split the data into training and test sets
X_train, X_test, y_train, y_test = custom_train_test_split(X_data, y_data, test_size=0.3, random_state=42)

# Predict the test set labels
test_predictions = nn_model.predict(X_test)

# Calculate evaluation metrics
true_positive = np.sum((test_predictions == 1) & (y_test == 1))
false_positive = np.sum((test_predictions == 1) & (y_test == 0))
false_negative = np.sum((test_predictions == 0) & (y_test == 1))
true_negative = np.sum((test_predictions == 0) & (y_test == 0))

precision_val = true_positive / (true_positive + false_positive) if (true_positive + false_positive) > 0 else 0
recall_val = true_positive / (true_positive + false_negative) if (true_positive + false_negative) > 0 else 0
f1_score_val = 2 * precision_val * recall_val / (precision_val + recall_val) if (precision_val + recall_val) > 0 else 0
accuracy_val = (true_positive + true_negative) / (true_positive + false_positive + false_negative + true_negative)

print("Precision:", precision_val)
print("Recall:", recall_val)
print("F1-Score:", f1_score_val)
print("Accuracy:", accuracy_val)

# Calculate loss
mean_squared_error_val = np.mean((test_predictions - y_test)**2)
print(f"MSE: {mean_squared_error_val}")

log_loss_val = np.mean(-y_test * np.log(nn_model.forward(X_test)) - (1 - y_test) * np.log(1 - nn_model.forward(X_test)))
print(f"log_loss: {log_loss_val}")
