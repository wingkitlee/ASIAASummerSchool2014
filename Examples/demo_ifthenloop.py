"""
Example script for if-then-else and for loop
"""

# import numpy module
import numpy as np

# this is a for loop
# range(10) is called an iterable, which is a list in this case
# range(10) = [0,1,...,9]
for i in range(10):
    # python 2 syntax
    print "i = ", i
    # with integer formating
    # %10i means 10 character space for an integer (right-aligned)
    print "i = %10i" % i
    
    # check if i is even or odd
    # mod -> remainder for i/2
    if np.mod(i,2)==0:
        print "%i is an even number."% i
    else:
        print "%i is an odd number." % i