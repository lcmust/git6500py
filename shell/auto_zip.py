#!/usr/bin/python
#coding=utf8
#filename:zuto_zip.py
#date:20121120-1300
#auth:http://segmentfault.com/q/1010000000142366
import os
import sys
import time
source_to_backup = ['/tmp']
dir_base = '/home/love/' # Remember to change this to what you will be using
# 3. The files are backed up into a zip file
# 4. The current day is the name of the subdirectory in the main directory
dir_today = dir_base + time.strftime('%Y%m%d')
# The current time is the name of the zip archive
now = time.strftime('%H%M%S')

# Create the subdirectory if it isn't already there
if not os.path.exists(dir_today):
        os.mkdir(dir_today) # make directory
        print '(%s) Successfully created directory' %(dir_today)
# The name of the zip file
backup_file_fullpath = dir_today +'/' + time.strftime('%Y%m%d%H%M%S') + '.zip'
# 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
zip_command = "zip -qr %s %s" % (backup_file_fullpath, ' '.join(source_to_backup))
#zip_command = "ls -lh"
# Run the backup
os.system(zip_command)

if os.path.exists(backup_file_fullpath):
    print 'Successful backup to',backup_file_fullpath
else:
    print 'check be carefull'
