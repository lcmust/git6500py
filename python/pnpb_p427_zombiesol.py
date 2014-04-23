#!/usr/bin/env python

import os, time, sys, signal

def childhandler(signum, stackframe):
    while True:
        try:
            result = os.waitpid(-1, os.WNOHANG)
        except:
            break
        print "Reaped child process %d" % result[0]
    signal.signal(signal.SIGCHLD, childhandler)

signal.signal(signal.SIGCHLD, childhandler)
print "Before the fork, my PID: %s" %(os.getpid())

pid = os.fork()
if pid:
    print "Hello from the parent. The child will be PID:%s" %(pid)
    print "sleeping 10 seconds...%s" %(time.asctime())
    time.sleep(10)
    print "Sleep done.%s" %(time.asctime())
    sys.exit(0)
else:
    print "Child sleeping 5 seconds...."
    time.sleep(5)
    sys.exit(0)
