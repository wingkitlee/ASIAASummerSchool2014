"""
Example script for using glob.glob utility

list the python files in the current directory
filter the ones with "demo_"
print the list
"""

# import glob module
import glob

# use the glob function
# pyfilelist is a list of python files
pyfilelist = glob.glob('*.py')

# for each entry in the file list, do blah blah blah
# now f is a string, which is the file name 
for f in pyfilelist:
    # if-clause can be used with string
    # if f contains 'demo_'
    if 'demo_' in f:
        print f
        
