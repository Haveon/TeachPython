#!/usr/bin/python3
import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt

data = np.loadtxt('data.csv', delimiter=',')   # Load the data in
x, y, xerr, yerr = data[:, 0], data[:, 1], data[:, 2], data[:, 3]    # Unpack it
slope, intercept, r, p, std = linregress(x,y)   # Get the slope and intercept

xs = np.linspace(0,50,2)     # Make dummy x and y to plot
ys = slope*xs + intercept    # line of best fit

plt.errorbar(x, y, yerr, xerr, 'o')    # Plot with the error bars, the 'o' just tells it to plot points not lines
plt.plot(xs,ys, label='$y = {} \cdot x + {}$'.format(slope, intercept))  # plot the lines of best fit and add a label
plt.legend(loc='best')   # Place the label in the best location
plt.xlabel('x')
plt.ylabel('y')
plt.tight_layout()    # I don't like wasted space, get rid of extra space

plt.savefig('Graph.png')   # save the figure, notice that it is before show
plt.show()   # if you call show before saving, you'll delete your plot before saving it
