#!/usr/bin/python

import os
import sys
from stat import *
import codecs

def dir_recursion( start, process, fix_order ):
    dirlist = os.listdir(start)
    for entry in dirlist:
        pathname = os.path.join(start, entry)
        mode = os.stat(pathname).st_mode
        if (S_ISREG(mode) and (pathname.endswith(".h") or pathname.endswith(".hpp") or pathname.endswith(".c") or pathname.endswith(".cpp"))):
            process(pathname, fix_order)
        elif S_ISDIR(mode):
            dir_recursion(pathname, process, fix_order)

def checkorderincludes( filename, fix_order ):
    linelistlib = []
    linelist = []
    qlinelist = []
    allines = []
    sourcefile = open(filename, "r+")
    for line in sourcefile:
        if (line.startswith("#include <Q")):
                qlinelist.append(line)
        elif (line.startswith("#include <")):
            linelistlib.append(line)
        elif (line.startswith("#include \"")):
            linelist.append(line)
        allines.append(line)
    sourcefile.close()
    
    if (fix_order):
        sort(linelistlib, filename, allines)
        sort(linelist, filename, allines)
    elif (not fix_order):
        disorder_out(linelistlib, filename)
        disorder_out(linelist, filename)

def disorder_out( stringlist, filename ):
    corrected_strings = []
    for string in stringlist:
        for strings in stringlist[stringlist.index(string):]:
            if (strings < string and strings not in corrected_strings):
                print (strings + " should come before " + string + " in " + filename)
                corrected_strings.append(strings)
def sort ( stringlist, filename, filelines ):
    corrected_strings = []
    for string in stringlist:
        for strings in stringlist[stringlist.index(string):]:
            if (strings < string and strings not in corrected_strings):
                filelines.remove(strings)
                filelines.insert(filelines.index(string), strings)
                corrected_strings.append(strings)
    if (len(corrected_strings) > 0):
        newfile = open(filename, "w")
        for stringline in filelines:
            newfile.write(stringline)
