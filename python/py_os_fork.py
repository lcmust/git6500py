#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys

def dothefork():
    pid = os.fork()
    if pid:
        return "parent"
    else:
        return "child"

if __name__ == "__main__":
    print "prog begin run...."
    print dothefork()
    print "prog will closing."
    sys.exit(0)
