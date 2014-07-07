from numpy import *
import pylab
import matplotlib.animation as animation

dt = 2.0*pi*0.005
t = arange(0.0, 5.0, dt)

Nr = 9

fig = pylab.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-3, 3), ylim=(-3, 3))
#ax.grid()
ax.set_aspect('equal')

circ = pylab.Circle((0.0,0.0), ls='dashed', radius=1, color='k', fill=False)
circ1 = pylab.Circle((0.0,0.0), ls='dashed', radius=2, color='k', fill=False)
ax.add_patch(circ)
ax.add_patch(circ1)

rl = linspace(1.0, 3.0, Nr)
ranphase = ones((Nr)) + random.random(Nr)*pi*2.0 
Npl = array([ int( 2.0*(Nr-1)*r) for r in rl])
Ntot= Npl.sum()
#cl = linspace(0.1, 1.0, Np)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def getxy(t,j,Np):
    """
        t: time
        r: radius
        Np: number of particle in the ring..
    """
    r = rl[j]
    p0 = ranphase[j]
    # plot a ring of particles
    omega0 = 2.0*pi # omega = 2pi / T
    
    pl = linspace(0.0, 2.0*pi, Np) + p0 #+ random.random()
    xy = zeros((Np,2))
    # angular rate, omega = omega0/r ; v=r*omega = const.
    
    omega = omega0/r - pi
    xy[:,0] = array([ r*cos(omega*t + p ) for p in pl])
    xy[:,1] = array([ r*sin(omega*t + p ) for p in pl])
    
    return xy

# colors
cl = zeros((Ntot))
for j in arange(Nr):
    Np = Npl[j]
    for k in arange(Np):
        cl[Npl[:j].sum()+k] = sin(float(k)/float(Np)*pi*2.0)
    
scat = ax.scatter(zeros((Ntot)),zeros((Ntot)),cmap=pylab.cm.gray)


def init():
    scat.set_offsets([])
    time_text.set_text('')
    return scat, time_text

def animate(i):
    xyl = zeros((Ntot, 2))
    for j in arange(Nr):
        Np = Npl[j]
        xy = getxy(t[i], j, Np)
        
        for k in arange(Np):
            xyl[Npl[:j].sum()+k,:] = xy[k,:]

    scat.set_offsets(xyl)
    time_text.set_text(time_template%(i*dt))
    return scat, time_text
                
ani = animation.FuncAnimation(fig, animate, arange(1, len(t)),
    interval=400, blit=True, init_func=init)

#mywriter = animation.MencoderWriter()
#ani.save('diffrot1.mp4', fps=15)

pylab.show()  

# test
#i=0
#xyl = zeros((Ntot, 2))
#for j, r in zip(arange(Nr),rl):
#    Np = Npl[j]
#    xy = getxy(t[i], r, Np)
#    
#    for k in arange(Np):
#        xyl[Npl[:j].sum()+k,:] = xy[k,:]
#print xyl