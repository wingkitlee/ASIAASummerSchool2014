from numpy import *
import pylab
import matplotlib.animation as animation

def singlehist2d(x,y, quad):
    counts, xedges, yedges, Image = pylab.hist2d(x,y,bins=20)
    quad.set_array(counts)
    return quad

fig = pylab.figure()
ax  = pylab.subplot(111)

ims = []
for ind in linspace(0.0,4.0,10):
    N = int(100*ind)
    x = random.randn(N)
    y = random.randn(N)
    
    ax.set_title('N = %i'%N)
     = pylab.hist2d(x,y,hold=False)
    ims.append((pylab.pcolor(xedges, yedges, counts),))
    
im_ani = animation.ArtistAnimation(fig, ims, interval=100, repeat_delay=3000,
    blit=True)

pylab.show()


