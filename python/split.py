#!/usr/bin/python
import re
fobj=open("input_file.txt","r")
for eachLine in fobj:
    #l = re.split(',', eachLine)
    l = eachLine.split(',')
    print l[2]
fobj.close()
