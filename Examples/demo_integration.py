import numpy as np
import pylab
from scipy.integrate import odeint

"""
Example for integration

coffee cooling problem:
    
integrate dT/dt = -k (T-Tout),

k is the cooling constant, in unit of min^-1
Tout is the environment temperature. When t is large, T-> Tout

"""

# parameters of the problem
# these values do not change
Tout = 20.0 # degree C
k    = 0.2  # 

# define the function for dT/dt
# can be array if it's a system of ODEs
def func(Temp,t):
    """
    dT/dt    
    """
    return -k*(Temp-Tout)
    
# initial condition
T0 = 90.0

# grid points for integration output
# t[0] is the initial time
t  = np.linspace(0.0,10.0,50)

# main integration routine
# return an array of shape (len(t),len(y0))
# in this case, res.shape = (len(t),1)
res = odeint(func,T0,t)

# get the Temp(t)
Temp = res[:,0]

pylab.plot(t,Temp)
pylab.xlabel('t [min]')
pylab.ylabel('Temperature [C]')
pylab.title('Coffee cooling problem')
pylab.show()



    
