#!/usr/bin/env python

import os, time, sys

print "Before the fork, my PID: %s" %(os.getpid())

pid = os.fork()
if pid:
    print "Hello from the parent. The child will be PID:%s" %(pid)
    print "sleeping 20 seconds..."
    time.sleep(20)
    sys.exit(0)
else:
    print "hello form the child."
    sys.exit(0)
