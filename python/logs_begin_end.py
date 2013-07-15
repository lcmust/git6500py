#!/usr/bin/python
#coding=utf8
#filename:logs_begin_end.py
#date:20121118-1300
#update:http://bbs.chinaunix.net/thread-4031117-1-1.html
import os
import sys
import time
time_start = time.time()
result = {}

if len(sys.argv) > 1: #第1个参数为源文件
    file_in = sys.argv[1]
    if (os.path.exists(file_in)):
        fd1 = open(file_in, 'r')
    else:
        print "source file(%s) is not exists, so exit!" % sys.argv[1]
        exit(-1)
else:
    print "please input the source file!"
    exit(-1)

def process(fd1):
    global result
    tmp3 = []
    for fileLine in fd1:
        tmp =  fileLine.strip()
        if tmp.startswith('#'): #去除行首以'#'开头的行（注释行）
            continue
        tmp3 = [tmp2.strip() for tmp2 in tmp.split(',') if tmp2]
        tmp_name = tmp3[0]
        tmp_date,tmp_time = tmp3[1].split()

        if tmp_name in result.keys():
            if tmp_date in result[tmp_name].keys():
                result[tmp_name][tmp_date] += [tmp_time]
            else:
                result[tmp_name][tmp_date] = [tmp_time]
        else:
            result[tmp_name] = dict(zip([tmp_date],[[tmp_time]]))

def process2():
    global result
    for tmp_name in result.keys():
        for tmp_date in result[tmp_name]:
            tmp_time = result[tmp_name][tmp_date]
            if len(tmp_time) == 1: #每天打卡时间只有1次
                if int(tmp_time[0].split(':')[0]) < 12:
                    print tmp_name + ',' + tmp_date + ',' + tmp_time[0] + ',miss'
                else:
                    print tmp_name + ',' + tmp_date + ',miss,' + tmp_time[0]
            elif len(tmp_time) == 2: #每天打卡时间正好2次
                print tmp_name + ',' + tmp_date + ',' + tmp_time[0] + ',' + tmp_time[1]
            elif len(tmp_time) > 2: #每天打卡时间为2次以上
                print tmp_name + ',' + tmp_date + ',' + tmp_time[0] + ',' + tmp_time[-1]

process(fd1)
'''由process(fd1)处理后的数据如下
{'wang wu': {'11/1/2012': ['9:00'], '11/2/2012': ['8:00', '8:05', '17:04']},
'zhang San': {'11/1/2012': ['8:00', '17:00'], '11/2/2012': ['17:05']},
'li si': {'11/1/2012': ['8:05', '17:03'], '11/2/2012': ['8:01', '16:59']}}
'''
process2()
'''经过process()处理后的数据如下
wang wu,11/1/2012,9:00,miss
wang wu,11/2/2012,8:00,17:04
zhang San,11/1/2012,8:00,17:00
zhang San,11/2/2012,miss,17:05
li si,11/1/2012,8:05,17:03
li si,11/2/2012,8:01,16:59
'''
time_end = time.time()
print "use time:%d seconds" % (int(time_end) - int(time_start))
