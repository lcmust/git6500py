#!/usr/bin/python
#coding=utf8
#filename: xlrd_xls2txt.py
#date: 20130411-1300
#auth: chengl6500
"""以下数字作为列宽标尺作用
12345678901234567890123456789012345678901234567890123456789012345678901234567890
"""

import os
import sys
import time
import xlrd

file1 = '/tmp/xls2txt3.txt'  #to write
file2 = '/home/love/20130410_KJJY.xls' #read from
try:
    txt1 = open(file1, 'w')
except IOError:
    print "open file %s ERROR!" %(file2)
    exit(-1)
try:
    xls = xlrd.open_workbook(file2)
except:
    print "open file %s ERROR!" %(file2)
    exit(-1)
sheet = xls.sheet_by_index(0)
sheet_nrows = sheet.nrows
sheet_ncols = sheet.ncols
for no_r in xrange(sheet_nrows):
    for no_c in xrange(sheet_ncols - 1):
        value = str(sheet.cell_value(no_r, no_c)).rstrip()
        #print '[' + str(no_r) + '][' + str(no_c) + ']:' + value,
        txt1.write(value)
        txt1.write('\t')
    #print '\n'
    txt1.write(str(sheet.cell_value(no_r, sheet_ncols - 1)))
    txt1.write('\n')
txt1.close()
