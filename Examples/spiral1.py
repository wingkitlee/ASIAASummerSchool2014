from numpy import *
import pylab

rl = linspace(0.1,1,20,endpoint=True)
tl = linspace(0.0,2.0*pi,100,endpoint=True)

fig = pylab.figure()
ax = fig.add_subplot(111)

for r in rl:
    phase = r*pi      # for systematic phase shift
    # phase = 0.0               # for no phase shift
    print phase
    xl = r*cos(tl)
    yl = 1.5*r*sin(tl)
    X = xl*cos(phase) - yl*sin(phase)
    Y = xl*sin(phase) + yl*cos(phase)
    pylab.plot(X, Y, 'k-')
    
ax.set_aspect('equal')
pylab.xlim(-1.5,1.5)
pylab.axis('off')
pylab.show()
    