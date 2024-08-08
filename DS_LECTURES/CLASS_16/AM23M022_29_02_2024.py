# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 09:57:00 2024

@author: mdine
"""

'''opengl - pygl ------graphics '''
'''  GUI - '''

import matplotlib.pyplot as  plt
import numpy as np
x = np.linspace(-5,5,100)
y=2*x**2
plt.plot(x,y,color  = "red", linewidth=2.5, markersize = 2)


x = np.arange(-2.0, 2.0, 0.01)
y = x ** 2
#Default is single figure
#fig, ax = plt.subplots()
#single axis
fig, ax = plt.subplots(2, 2, figsize = (4,4))
print(type(fig))
print(type(ax))
ax.plot(x,y)


x1 = np.linspace(-4 * np.pi, 4 * np.pi, 100)
y1 = np.sin(x1)
# plt.plot(x1, y1, '-', color='blue', lw = 1.5, ms = 2, label = 'sin crv')
# plt.legend(loc='upper right', fontsize = 10)

m_fig, m_axes = plt.subplots(2, 2, figsize = (8,4))
ax = m_axes[0][0]
ax.plot(x,y)

ax = m_axes[0][1]
ax.plot(x1,y1)

t = np.arange(-2.0, 2.0, 0.1)
x = t
y = t ** 2
z = t ** 3

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# ax = m_axes[1][0]
ax.plot(x, y, z)




#Changing the above for the contour part
x = np.arange(-2.0, 2.0, 0.1)
y = np.arange(-2.0, 2.0, 0.1)
# The following will print a 3D surface
X,Y=np.meshgrid(x,y) #Forming MeshGrid
Z = X**3
#Z = X **2 + Y ** 2
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

'''Contour plot - level setter '''

fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

#ax.plot_surface(X, Y, Z)
cp  = plt.contour(x, y, Z)
plt.clabel(cp, fontsize=8)
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')

plt.show()