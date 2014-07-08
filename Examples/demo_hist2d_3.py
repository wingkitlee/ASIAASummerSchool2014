from numpy import *
import pylab

# number of data in each dimension
N = 2000

x = random.randn(N)
y = random.randn(N)

# make the histogram (without plotting)
H, xedges, yedges = histogram2d(x,y,bins=50)

# mask out the array
Hmasked = ma.masked_less(H, 0.01) # ignore where value < 0.01

# generate the mesh for 2D plotting
X, Y = meshgrid(xedges,yedges)

pylab.pcolormesh(X,Y,Hmasked)
pylab.xlim(-5.0,5.0)
pylab.ylim(-5.0,5.0)
pylab.show()
