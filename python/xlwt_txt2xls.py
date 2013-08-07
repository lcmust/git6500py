#!/usr/bin/python
#coding=utf-8
#filename: xlwt_txt2xls.py
#保存IIS的日志文件（文本）为XLS表格，使用xlwt/xlrd限制XLS表格的行不能走过65535行
#date: 20130726-1300
#auth: chengl6500
"""以下数字作为列宽标尺作用
12345678901234567890123456789012345678901234567890123456789012345678901234567890
"""

import os
import sys
import time
import xlrd
import xlwt

print time.ctime()
f_txt2xls = '/tmp/txt2xls.xls'
f_txt_from = '/home/love/scxhedu_ex130706.log'

try:
    txt_from = open(f_txt_from)
except IOError:
    print "open file %s ERROR!" %(f_txt_from)
    exit(-1)

xls_book = xlwt.Workbook()
xls_book_sheet1 = xls_book.add_sheet('sheet1')
line_no = 0

def write_sheet(txtFrom, xls_to, lineNo):
    row = 0
    for tmp in txtFrom.split():
        xls_to.write(lineNo, row, tmp)
        row += 1


txt_from_iter = iter(txt_from)
while True:
    try:
        txt_proc = txt_from_iter.next().decode('utf-8', 'ignore')
        #txt_proc = txt_from_iter.next().decode('utf-8')
    except StopIteration:
        break

    write_sheet(txt_proc, xls_book_sheet1, line_no)
    if line_no == 65535:
        break
    line_no += 1

xls_book.save(f_txt2xls)
print time.ctime()


"""
-rw-r--r-- 1 love love 78176392  7月  6 22:31 scxhedu_ex130706.log
-rw-r--r-- 1 love love 14446592  7月 27 15:29 txt2xls.xls
Sat Jul 27 15:29:30 2013
Sat Jul 27 15:29:53 2013

Sat Jul 27 15:31:17 2013
Sat Jul 27 15:31:44 2013
"""
