"""
Example script for plotting histogram 
"""

# import every function from numpy module
# can use the function directly from now
from numpy import *
# import pylab module
# use pylab.function to call 
import pylab

# generating data
# number of data points in each dimension
N = 4000
# sigma of normal distribution
sigma = 1.0
# mean position of normal distribution,
# mu_x = 0.0
# mu_y = 0.0

# random number from "normal" distribution
# default: sigma = 1.0, mean = 0.0
# if using import numpy as np, call np.random.randn
x = sigma*random.randn(N)
y = sigma*random.randn(N)

# for contour
# define x, y axis
xi = linspace(-4.0,4.0,200)
yi = linspace(-4.0,4.0,200)
# get the 2D array 
X,Y = meshgrid(xi,yi)
R = sqrt(X**2 + Y**2)
Z = (1.0/sigma/sqrt(2.0*pi))*exp(-0.5*(R/sigma)**2)




# figsize in inches
fig = pylab.figure(1, figsize=(12,6))

# subplot: multiple plots within single figure
# return the axes
# 121 -> nrow=1, ncol=2, id=1
ax1 = pylab.subplot(121)
# short cut to plot a histogram
pylab.hist2d(x,y,bins=50,cmin=0.01)

# return the axes
# 122 -> nrow=1, ncol=2, id=2
ax2 = pylab.subplot(122)
# contours
pylab.imshow(Z,extent=[-4.0,4.0,-4.0,4.0])
#pylab.colorbar()
pylab.contour(X,Y,Z,3,colors='w')
#pylab.colorbar()



## gca() = get current axes
## possible to have many subplots and axes in one figure
#ax = pylab.gca()
## (re)set the aspect ratio of the current plot
#ax.set_aspect(1.0)

# alternative way to define labels
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax2.set_xlabel('x')
ax2.set_ylabel('y')

# define limits
pylab.xlim(-4.0,4.0)
pylab.ylim(-4.0,4.0)

ax1.set_xlim(-4.0,4.0)
ax1.set_ylim(-4.0,4.0)
ax1.set_aspect(1.0)

# show() is required if using in non-interactive environment
pylab.show()