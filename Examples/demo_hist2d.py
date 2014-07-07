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
N = 20000

# random number from "normal" distribution
# default: sigma = 1.0, mean = 0.0
x = random.randn(N)
y = random.randn(N)

# short cut to plot a histogram
pylab.hist2d(x,y,bins=50,cmin=0.0001)

# show() is required if using in non-interactive environment
pylab.show()