#!/usr/bin/python3
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def dydx(y,x):
    """
    Make a function that takes in two values, y and x,
    and then returns $\\frac{dy}{dx}$
    """
    return -y*np.sin(y)

xs = np.linspace(0, 2*np.pi, 1000)    # The domain we want the solution over

y0 = -0.5    # The first initial condition
sol1 = odeint(dydx, y0, xs)   # Use odeint to solve the problem

y0 = 1    # The second set of initial conditions
sol2 = odeint(dydx, y0, xs)   # Again using odeint

plt.subplot(211)   # Make a subplot with 2 rows and 1 column, start at the first axis
plt.plot(xs,sol1)
plt.title('Initial condition: $y(0) = -0.5$')

plt.subplot(212)   # Move to the second axis
plt.plot(xs,sol2)
plt.title('Initial condition: $y(0) = 1$')

plt.tight_layout()
plt.show()
