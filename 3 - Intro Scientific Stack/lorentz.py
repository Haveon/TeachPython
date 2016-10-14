#! /usr/bin/python3

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D    # Remember to import the 3D axes!

# Initialize these constants
sigma = 10
beta = 8/3
rho = 28

def derivatives(vector,t):
    x, y, z = vector   # Unpack the vector

    # Calculate each derivative in order
    x_prime = sigma*(y-x)
    y_prime = x*(rho - z) - y
    z_prime = x*y - beta*z

    return np.array([x_prime, y_prime, z_prime])    # Repackage the derivatives

vector0 =  np.array([2, 3, 4])   # The initial conditions
ts = np.linspace(0,20,1000)      # The domain we want the solution in

sol = odeint(derivatives, vector0, ts)   # solve with odeint

xs = sol[:,0]   # Unpack by using numpy indexing
ys = sol[:,1]   # We all the values of the 0th, 1st
zs = sol[:,2]   # and second column respectively

fig = plt.figure()
fig.add_subplot(111, projection='3d')   # Don't forget to add a 3d axes!
plt.plot(xs, ys, zs)
plt.tight_layout()
plt.show()
