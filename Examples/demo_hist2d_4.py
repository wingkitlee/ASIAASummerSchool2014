"""
Example script for animating histogram function

Kit, wklee (at) asiaa
ref:
    https://stackoverflow.com/questions/21487916/animating-a-quadmesh-from-pcolormesh-with-matplotlib
"""

# usual stuff to import
from numpy import *
import pylab

# import animation module
import matplotlib.animation as animation

# create a figure
fig = pylab.figure()
# get the axis
ax = pylab.subplot(111)

#pylab.hold(True)


# contour stuff
xc = linspace(-5.0,5.0,50)
yc = linspace(-5.0,5.0,50)
XX, YY = meshgrid(xc,yc)
R = sqrt(XX**2+YY**2)
Z = exp(-0.5*R**2)
p = pylab.contour(XX,YY,Z)

# initial function
def init():
    # clear the current figure
    pylab.hold(False)
    fig.clf()
    

# main function to animate
def animate(i):
    # number of data in each dimension
    # N = 200000
    fig.clf()
    pylab.hold(True)
    N = int(10**(i/2.0))
    x = random.randn(N)
    y = random.randn(N)
    
    # make title
    ax = pylab.gca()
    
    # make the histogram (without plotting)
    xyrange = [[-5.0,5.0],[-5.0,5.0]]
    H, xedges, yedges = histogram2d(x,y,range=xyrange, bins=51)
    
    # mask out the array
    Hmasked = ma.masked_less(H, 0.01) # ignore where value < 0.01
    
    # generate the mesh for 2D plotting
    X, Y = meshgrid(xedges,yedges)
    pylab.pcolormesh(X,Y,Hmasked)
    
    # contour
    ax.contour(XX,YY,Z,4,colors='w',ls=2)
    
    ax.set_xlim(-5.0,5.0)
    ax.set_ylim(-5.0,5.0)
#    pylab.ylim(-5.0,5.0)
#    pylab.draw()
    pylab.hold(False)



anim = animation.FuncAnimation(fig, animate, init_func=init,\
    frames = range(5,12), blit=False, interval=200, repeat=True)

pylab.show()
# set the hold state to off
# it's required when you want to clear the figure and release the memory
pylab.hold(False)