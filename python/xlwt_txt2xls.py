#!/usr/bin/python
#coding=utf8
#filename:xlwt_txt2xls.py
#date:20130411-1300
#auth:chengl6500
"""以下数字作为列宽标尺作用
12345678901234567890123456789012345678901234567890123456789012345678901234567890
"""

import os
import sys
import time
import xlwt

file1 = '/tmp/xls2txt3.txt' #read from
file2 = '/tmp/txt2xls.xls' #to write
try:
    txt1 = open(file1)
except IOError:
    print "open file(%s) ERROR!" %(file1)
    exit(-1)
wb = xlwt.Workbook()
sheet = wb.add_sheet('sheet1')
row, col = 0, 0
while(1):
    conts = txt1.readline()
    if conts:
        cont_rows = conts.split('\t')
        print '\n', cont_rows,'\n'
        for cont_row in cont_rows:
            #print '\t', cont_row
            print str(row) + '/' + str(col),
            sheet.write(row, col, str(cont_row.rstrip()))
            col += 1
        row += 1
        col = 0
    else:
        break
wb.save(file2)
txt1.close()
