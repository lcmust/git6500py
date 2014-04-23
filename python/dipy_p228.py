#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import getopt
import urllib2
import httplib

def usage():
    print "help msg"
    
def process_argv(argv):
    url = ""
    try:
        opts, args = getopt.getopt(argv, "hu:d", ["help", "url="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt == "-d":
            global _debug
            _debug = 1
        elif opt in ("-u", "--url"):
            url  = arg
    source = ''.join(args)
    return source, url

def test(url=None, debug=0):
    if url == None:
        return
    ## fsock_g = stdout_to_file()
    httplib.HTTPConnection.debuglevel = debug
    if httplib.HTTPConnection.debuglevel:
        print httplib.HTTPConnection.debuglevel
    request = urllib2.Request(url)
    opener = urllib2.build_opener()
    feeddata = opener.open(request).read()
    ## sys.stdout.write("test")
    ## stdout_to_reset(fsock=fsock_g)
    return feeddata

def stdout_to_file(filename="/tmp/py_test.log"):
    global save_stdout
    global save_stderr
    save_stdout = sys.stdout
    save_stderr = sys.stderr
    fsock = open(filename, 'a+')
    sys.stdout = fsock
    sys.stderr = fsock
    return fsock

def stdout_to_reset(fsock=None):
    if fsock == None:
        return
    global save_stdout
    global save_stderr
    sys.stdout = save_stdout
    sys.stderr = save_stderr
    fsock.close()

    
if __name__ == "__main__":
    _debug = 0
    save_stdout = ""
    save_stderr = ""
    httplib.HTTPConnection.debuglevel = 1
    request = urllib2.Request("http://192.168.0.1")
    opener = urllib2.build_opener()
    feeddata = opener.open(request)
