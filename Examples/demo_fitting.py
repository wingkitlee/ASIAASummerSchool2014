"""
Example for fitting

Jul 14, 2014
Kit wklee (at) asiaa
"""

# usual import for numpy and pylab
from numpy import *
import pylab

# curve_fit: curve fitting module from scipy
from scipy.optimize import curve_fit

# to use latex for text,
# may not work in linux if there is not latex installed
pylab.rc('text',usetex=True)

# define a fitting function
def func(x, a, b, c, d):
    return a*sin(b*x+c)+d

# number of grid points
N = 200

# data
x = linspace(0.0,1.0,N)
y = sin(x*2.0*pi)+0.5*random.randn(N)

# to fit the data with the defined function "func"
# i.e., determine the values of parameters
popt, pconv = curve_fit(func, x, y)

# print out some results
print "result:"
print "fitting using f(x) = a*sin(b*x+c)+d"
print "amplitude, a = ", popt[0]
print "period   , b = ", popt[1]
print "phase    , c = ", popt[2]
print "offset   , d = ", popt[3]

# generate the data points from the fitted parameters
# "*popt" is a shorthand for multiple arguments
yfit = func(x, *popt)

# plot data
pylab.plot(x,y,'.')
# plot fitting function
pylab.plot(x,yfit,'k-',lw=3)

pylab.xlabel('time, t [s]')
pylab.show()