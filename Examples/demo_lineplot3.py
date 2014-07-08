import numpy as np
import pylab

"""
http://mathworld.wolfram.com/FourierSeriesSquareWave.html
"""

# half box length
L = 1.0
# number of points
N = 200

def FourierComp(x,n):
    f = 4.0/(np.pi*n)*np.sin(n*np.pi*x/L)
    return f
    
def FourierSeries(x,n):
    """
    Sum up the odd number within n
    """
    ysum = np.zeros_like(x)
    for i in range(1,n+1,2):
        ysum = ysum + FourierComp(x,i)
    return ysum
        

# x-dimension
x = np.linspace(0.0,2.0*L,N)
# square wave
# make an array of 1, with length = N (same as x)
ysquare = np.ones_like(x)
# change the elements where x>L to -1.0
ysquare[x>L] = -1.0

#
y1 = FourierSeries(x,1)
y3 = FourierSeries(x,3)
y5 = FourierSeries(x,5)
y7 = FourierSeries(x,7)

pylab.plot(x,ysquare,'k-', lw=3)
pylab.plot(x,y1,'-')
pylab.plot(x,y3,'--')
pylab.plot(x,y5,'-.')
pylab.plot(x,y7,':')
#pylab.plot(x,ysum,'--')

pylab.ylim(-1.5,1.5)

pylab.xticks((0.0,L,2.0*L),['0','L','2L'])

pylab.title('Fourier Series of a Square Wave')

pylab.show()