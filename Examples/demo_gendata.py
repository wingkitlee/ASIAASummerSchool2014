"""
Example script for generating some data
"""

# numpy for numerical stuff
import numpy as np
# sys for reading the command line argument
import sys

# simple command line arguement setup
# e.g., python something.py 10 
# -> sys.argv = ['something.py', '10']
if len(sys.argv) != 2:
    # print usage if not in correct format
    print "Usage: python demo_gendata.py N"
    print "where N is the number of data points"
    sys.exit()
else:
    # get the number of points
    N = int(sys.argv[1])
    print "Number of points = ", N

# generate the data
x = np.random.random(N)
y = np.random.random(N)

# open a file, in 'write' mode
# write the position pair into file
# close file
f = open('test.dat','w')
for i in range(N):
    f.write("%10.4f %10.4f\n" % (x[i],y[i]))
f.close()