# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:26:32 2024

@author: mdine
"""


'''2.Using steepest gradient descent, find all the local minima for the function
  J(x1, x2) = (x1^2+x2−11)^2+(x1+x2^2−7)^2. While applying gradient descent, do the following
  (a) Fixing the value for alpha (b) use line search to determine the value for alpha. Plot the intermediate
  steps in the iteration to show one of the minimal point. '''

'''-----------------------------------------------------------------'''

import numpy as np
import matplotlib.pyplot as plt

def J(x1, x2):
    return (x1**2 + x2 - 11)**2 + (x1 + x2**2 - 7)**2

x1 = np.linspace(-5, 5, 100)
x2 = np.linspace(-5, 5, 100)
x1, x2 = np.meshgrid(x1, x2)

plt.figure()
contour = plt.contour(x1, x2, J(x1, x2), levels=100)
plt.clabel(contour)
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Contour plot")

# Define the gradient function using numerical differentiation
def grad_J(x1, x2, h=1e-5):
    grad_x1 = (J(x1 + h, x2) - J(x1, x2)) / h
    grad_x2 = (J(x1, x2 + h) - J(x1, x2)) / h
    return np.array([grad_x1, grad_x2])

# Define the gradient descent algorithm with trajectory recording
def grad_descent_with_trajectory(starting_point, alpha=0.01, max_iterations=50, epsilon=1e-6):
    # Starting point
    x1, x2 = starting_point
    iteration = 0
    
    trajectory = [(x1, x2)]
    
    while iteration < max_iterations:
        # Compute gradient
        grad = grad_J(x1, x2)
        
        # Update parameters
        x1 -= alpha * grad[0]
        x2 -= alpha * grad[1]
        
        # Record trajectory
        trajectory.append((x1, x2))
        
        # Check for stopping criteria
        if np.linalg.norm(grad) < epsilon:
            break
        
        iteration += 1
    
    return trajectory

# Define starting points
starting_points = [(1, 2), (-3, 0), (-4, -4), (4, -4), (0, 0)]

# Plot trajectory for each starting point
for start_point in starting_points:
    trajectory = grad_descent_with_trajectory(start_point)
    x1_vals, x2_vals = zip(*trajectory)
    plt.plot(x1_vals, x2_vals, 'ro-')

plt.show()

'''2b'''

import matplotlib.pyplot as plt
import numpy as np


def j(w1, w2):
     # return (w1 - 8) ** 2 + (w2 - 10) ** 2
     return  (w1**2 +w2 -11)**2+(w1+ w2**2 -7)**2
def j1(w1,w2,grad_array):
    h=0.001
    r1=j(w1+h,w2)-j(w1-h,w2)
    r1=r1/(2*h)
    r2=j(w1,w2+h)-j(w1,w2-h)
    r2=r2/(2*h)
    res1=[r1,r2]
    grad_array.append(res1)
    return grad_array
    
   
def weight_update(grad_array,weight_array):
    # g1,g2=grad_array[-1]
    
    w1,w2= weight_array[-1]
    g=j1(w1,w2,grad_array)
    g1,g2=g[-1]
    # w1=a;w2=b
    a=0.00001 ;b=0.01
    # a=0 ;b=0.01;n=5000
    # a=0;b=1
    alpha=halving(a,b,grad_array,weight_array)
    print(alpha)
    w1=w1-alpha*g1
    w2=w2-alpha*g2
    res=[w1,w2]
    weight_array.append(res)
    return weight_array,g
    
def terminate(grad_array,iter1):
     if len(grad_array)<3:
         stop=0
         
     else:
         g1_new, g2_new=grad_array[-1]
         g1_old, g2_old=grad_array[-2]
         check=g1_new*g1_old+g2_new*g2_old
         stop=0
         if check<0.05:
            stop=1
     return stop

def plot_contour():
   w1 = np.linspace(-5, 5, 500)
   w2 = np.linspace(-5, 5, 500)
   W1, W2 = np.meshgrid(w1, w2)
   Z = j(W1, W2)
   plt.contour(W1, W2, Z, levels=50)

def halving(a,b,g,w):
    def term(a,b):
        l=(b-a)
        e= 1e-5
        if abs(l)<e:
            stop=1
            return a,b,stop
        else:
            w1=a+l/4
            w2=b-l/4
            stop=0
            return w1,w2,stop
    # a=2;  b=4;    e=0.0005
    l=b-a;wm=(a+b)/2
    stop=0
    while(stop==0):
        # print('s')
        w1=a+l/4
        w2=b-l/4
        if k(w1,g,w)<k(wm,g,w):
            b = wm
            wm= w1
            w1,w2,stop=term(a,b)
        elif  k(w2,g,w)<k(wm,g,w):
            a = wm
            wm=w2
            w1,w2,stop=term(a,b)
        else:
            a=w1
            b=w2
            w1,w2,stop=term(a,b)    
    alpha=wm
    return alpha
def k(a,g,w):
    w1,w2=w[-1]
    g1,g2=g[-1]
    w1=w1+a*g1 
    w2=w2+a*g2
    #print(w1,w2,g1,g2)
    return j(w1,w2)
    
    
stop=0   
iter1=0 
# alpha=0.001
# grad_array=[[0.1,0.1]]
grad_array=[]
weight_array=[[-2,-1]]
while (stop==0):
    # w1=1;w2=1
    
    iter1=iter1+1
    w,g=weight_update(grad_array,weight_array)
    stop=terminate(g,iter1)
    # alpha=alpha_update(alpha,w,g)
plot_contour()
w1=[i[0] for i in weight_array]
w2=[i[1] for i in weight_array]


plt.plot(w1, w2, color='r')
plt.title('contour plot')
plt.xlabel('w1')
plt.ylabel('w2')
plt.grid(True)
plt.show()
