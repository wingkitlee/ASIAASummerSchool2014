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
N = 2000
# sigma of normal distribution
sigma = 1.0
# mean of normal distribution
mu = 0.0

# random number from "normal" distribution
# default: sigma = 1.0, mean = 0.0
x = sigma*random.randn(N)+mu
y = sigma*random.randn(N)+mu

# figsize in inches
fig = pylab.figure(1, figsize=(6,6))

# short cut to plot a histogram
pylab.hist2d(x,y,bins=50,cmin=0.0001)

## gca() = get current axes
## possible to have many subplots and axes in one figure
#ax = pylab.gca()
## (re)set the aspect ratio of the current plot
#ax.set_aspect(1.0)

# define labels
pylab.xlabel('x')
pylab.ylabel('y')

# define limits
pylab.xlim(-4.0,4.0)
pylab.ylim(-4.0,4.0)

# show() is required if using in non-interactive environment
pylab.show()