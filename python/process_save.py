#!/usr/bin/python
#coding=utf-8
#第2次运行本脚本后，保存的进度文件中会包含字符^@^@    ???????20131107
#对原文件数据读取后，保存新的数据到文件（改写文件），读取文件后，关闭文件，重新以“w“写入方式打开文件，然后保存新的数据20131110
import os
import sys
import datetime

print datetime.datetime.now(), "Begin...."
# ready to work
if len(sys.argv) > 3:
    file_pwd = sys.argv[1]
    file_proc = sys.argv[2]
    process_nos = int(sys.argv[3])
elif len(sys.argv) > 2:
    file_pwd = sys.argv[1]
    file_proc = '/home/love/process_how.txt'
    process_nos = int(sys.argv[2])
elif len(sys.argv) > 1:
    file_pwd = '/home/love/dic.txt'
    file_proc = '/home/love/process_how.txt'
    process_nos = int(sys.argv[1])
else:
    print "cmd: argv1 argv2 argv3\n"
    process_nos = int(raw_input())
    file_pwd = '/home/love/dic.txt'
    file_proc = '/home/love/process_how.txt'
    # exit(1)
if os.path.exists(file_proc):
    fd_proc = open(file_proc, 'r+')
    file_proc_cont = fd_proc.readline()
    if file_proc_cont:
        file_proc_cont = file_proc_cont.rstrip()
        # print 'DEBUG:', file_proc_cont, len(file_proc_cont), type(file_proc_cont)
        for tmp in file_proc_cont:
            if  '9' < tmp < '0':
                exit(1)
            else:
                # print tmp, type(tmp)
                pass
        process_how = int(file_proc_cont)
    else:
        process_how = 0
else:
    fd_proc = open(file_proc, 'w')
    process_how = 0

if os.path.exists(file_pwd):
    fd_pwd = open(file_pwd, "r")
    if process_how > 0:
        fd_pwd.seek(process_how)
        # print 'fd_pwd: ', fd_pwd.readline()
        
# work begin
# test--------------
test = 3
for tmp in range(process_nos):
    fd_pwd_cont = fd_pwd.readline()
    if not fd_pwd_cont:
        exit(1)
    print 'now: ', fd_pwd_cont, 'fd_pwd.tell(): ', fd_pwd.tell()
else:
    fd_proc.close()
    fd_proc = open(file_proc, 'w')
    fd_index = fd_pwd.tell()
    print fd_index, 'type:', type(fd_index), int(fd_index), type(int(fd_index)), str(fd_index)
    fd_proc.write(str(fd_index) + '\n')
    fd_proc.close()
    fd_pwd.close()

if __name__ == "__main__":
    print datetime.datetime.now()
