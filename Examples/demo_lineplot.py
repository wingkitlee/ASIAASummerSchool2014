"""
Example script for producing line plots
"""
# import everything from numpy
# recommend only for plotting files
from numpy import *

# import pylab or matplotlib for plotting routines
import pylab

# generate some data
# linspace and sin are functions in numpy, but no prefix needed if we
# import *
x1 = linspace(0.0,1.0,100)
y1 = sin(x1*2.0*pi)
y2 = sin(x1*4.0*pi)
y3 = sin(x1*6.0*pi)
y4 = sin(x1*8.0*pi)

# plotting
pylab.plot(x1,y1)
pylab.plot(x1,y2)
# linestyle can be '-', '--', '-.' or ':'
#pylab.plot(x1,y3,'k-')
#pylab.plot(x1,y4,'k--')
#pylab.plot(x1,y2,'.')

# output
# show() or savefig()
# show() will produce figure on screen
# savefig('file') will save figure to file
pylab.show()
#pylab.savefig('test.png')
