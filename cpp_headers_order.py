'''
Documentation, License etc.

@package cpp_headers_order
'''
import os
import sys
from stat import *

import includesorder

startpath = os.getcwd()
sort = False

for arg in sys.argv:
    if (arg == "--start-dir"):
        startpath = sys.argv[sys.argv.index(arg) + 1]
    if (arg == "--fix"):
        sort = True
        
        
if S_ISREG(os.stat(startpath).st_mode):
    includesorder.checkorderincludes( startpath, sort )
elif S_ISDIR(os.stat(startpath).st_mode):
    includesorder.dir_recursion(startpath, includesorder.checkorderincludes, sort)
else:
    print (startpath + " is not a valid path to file or directory.  Please try again")
