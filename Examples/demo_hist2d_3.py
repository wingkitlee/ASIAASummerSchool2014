from numpy import *
import pylab

# number of data in each dimension
N = 2000

# normal distribution
x = random.randn(N) + 1.0
y = random.randn(N) + 2.0

# make the histogram (without plotting)
H, xedges, yedges = histogram2d(x,y,bins=50)

# rotation and flipping needed for correct orientation
# need check
H = rot90(H)
H = flipud(H)

# mask out the array
Hmasked = ma.masked_less(H, 0.01) # ignore where value < 0.01

# generate the mesh for 2D plotting
X, Y = meshgrid(xedges,yedges)

pylab.pcolormesh(X,Y,Hmasked)
pylab.xlim(-5.0,5.0)
pylab.ylim(-5.0,5.0)
pylab.show()
