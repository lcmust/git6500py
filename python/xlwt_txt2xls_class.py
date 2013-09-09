#!/usr/bin/python
#coding=utf-8
#filename: xlwt_txt2xls_class.py
#保存IIS的日志文件（文本）为XLS表格(使用xlwt/xlrd限制XLS表格的行不能超过65535行)
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

class WriteXls2003():
    # txt_file = None
    # xls_file = None
    # xls_book = None

    def __init__(self, xls_file=None, txt_file=None):
        if not xls_file or not txt_file:
            return

        if not os.path.exists(txt_file):
            return

        if os.path.exists(xls_file):
            xls_file_bak = xls_file + time.strftime("%Y%m%d_%H%M%S")
            os.rename(xls_file, xls_file_bak)

        self.txt_file = txt_file
        self.xls_file = xls_file
        self.xls_book = xlwt.Workbook()
        self.xls_book_sheet = self.xls_book.add_sheet('sheet1')
        self.lineNo = 0

    def open_txt(self, txt_file=None):
        if not txt_file:
            txt_file_from = self.txt_file

        try:
            txt_from = open(txt_file_from)
        except IOError:
            print "open file %s ERROR!" %(txt_file_from)
            exit(-1)

        self.txt_from = txt_from
        return
        #return txt_from

    def add_sheet(self, xls_book=None, sheet_name=None):
        if not xls_book:
            xls_book = self.xls_book

        if not sheet_name:
            sheet_name = time.strftime("%Y%m%d%H%M%S")

        return xls_book.add_sheet(sheet_name)

    def del_sheet(self, sheet_name=None):
        if not sheet_name:
            return
        return "have not finish it!"

    def write_sheet_col(self, txt_from, xls_to, lineNo):
        col = 0
        for tmp in txt_from.split():
            xls_to.write(lineNo, col, tmp)
            col += 1

    def write_sheet(self, txt_from=None, xls_to=None, lineMax=65535):
        if not txt_from:
            txt_from = self.txt_from

        if not xls_to:
            xls_to = self.xls_book_sheet

        txt_from_iter = iter(txt_from)
        while True:
            try:
                txt_proc = txt_from_iter.next().decode('utf-8', 'ignore')
            except StopIteration:
                break
            self.write_sheet_col(txt_proc, xls_to, self.lineNo)
            self.lineNo += 1
            if self.lineNo == lineMax:
                break
            #print self.lineNo

    def save_book(self, xls_book=None, file_to_save=None):
        if not xls_book:
            xls_book = self.xls_book

        if not file_to_save:
            file_to = self.xls_file

        xls_book.save(file_to)

if __name__ == "__main__":
    time_start = time.ctime()
    print "time is %s, beginning......\n" % time_start
    inst1 = WriteXls2003("/tmp/xls1.xls", "/home/love/scxhedu_ex130706.log")
    inst1.open_txt()

    #xls_sheet = inst1.add_sheet('sheet1')
    #inst1.write_sheet(txt_file, inst1.xls_book_sheet)

    inst1.write_sheet(lineMax=65535)
    time_save = time.ctime()

    #inst1.save_book(inst1.xls_book, inst1.xls_file)
    inst1.save_book()
    time_end = time.ctime()
    print "end@", time_end, '\nsave@', time_save, '\nstart@', time_start

"""
-------------NEW--------
end@ Mon Jul 29 18:13:45 2013
save@ Mon Jul 29 18:13:42 2013
start@ Mon Jul 29 18:13:19 2013
===============OLD=====
-rw-r--r-- 1 love love 78176392  7月  6 22:31 scxhedu_ex130706.log
Sat Jul 27 15:27:01 2013
Sat Jul 27 15:27:28 2013
-rw-r--r-- 1 love love  14M  7月 27 15:27 xls1.xls
"""
