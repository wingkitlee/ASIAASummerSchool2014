"""
Example script for reading data and plotting it

it reads
"""

import numpy as np
# use pylab or matplotlib for plotting
import pylab

# define a routine for plotting some data
def plotdata(data):
    x = data[:,0]
    y = data[:,1]
    pylab.scatter(x,y)
    
# the following statement makes this python file 'import-able'
# from other python file without running the main script
if __name__=='__main__':
    import sys
    # simple command line arguement setup
# e.g., python something.py 10 
# -> sys.argv = ['something.py', '10']
    if len(sys.argv) != 2:
        # print usage if not in correct format
        print "Usage: python demo_readdata.py test.dat"
        print "where test.dat is the name of the data file"
        sys.exit()
    else:
        # get the data file
        datafile = sys.argv[1]
        
    # read the data    
    data = np.genfromtxt(datafile)
    
    # print some info
    print "number of points = ", data.shape[0]
    
    # plotting
    plotdata(data)
    
    # show the figure
    pylab.show()