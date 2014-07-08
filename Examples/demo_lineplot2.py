import numpy as np
import pylab

"""
http://mathworld.wolfram.com/FourierSeriesSquareWave.html
"""

# half box length
L = 1.0
# number of points
N = 100

def FourierComp(x,n):
    f = 4.0/(np.pi*n)*np.sin(n*np.pi*x/L)
    return f

# x-dimension
x = np.linspace(0.0,2.0*L,N)
# square wave
ysquare = np.ones_like(x)
ysquare[x>L] = -1.0

y1 = FourierComp(x,1)
y3 = FourierComp(x,3)
y5 = FourierComp(x,5)
y7 = FourierComp(x,7)

ysum= y1+y3+y5+y7

pylab.plot(x,ysquare,'k-', lw=3)
pylab.plot(x,y1,'--')
#pylab.plot(x,y3,'--')
pylab.plot(x,ysum,'--')

pylab.ylim(-1.5,1.5)
pylab.show()