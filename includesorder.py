#!/usr/bin/python

import os
import sys
from stat import *

def dir_recursion( start, process ):
    dirlist = os.listdir(start)
    for entry in dirlist:
        pathname = os.path.join(start, entry)
        mode = os.stat(pathname).st_mode
        if S_ISREG(mode):
            process(pathname)
        elif S_ISDIR(mode):
            dir_recursion(pathname, process)

def checkorderincludes( filename ):
    linelistlib = []
    linelist = []
    sourcefile = open(filename, "r+")
    for line in sourcefile:
        if (line.startswith("#include <")):
            linelistlib.append(line)
        if (line.startswith("#include \"")):
            linelist.append(line)
    sourcefile.close()

    sort(linelistlib, filename)
    sort(linelist, filename)

def sort( stringlist, filename ):
    corrected_strings = []
    for string in stringlist:
        for strings in stringlist[stringlist.index(string):]:
            if (strings < string and strings not in corrected_strings):
                print (strings + " should come before " + string + " in " + filename)
                corrected_strings.append(strings)

dir_recursion(sys.argv[1], checkorderincludes)
