#!/usr/bin/env python
#coding=utf-8

def file_f(filename):
    print "filename:", file
    hosts = file(filename)
    try:
        for line in hosts:
            if line.startswith('#'):
                continue
            print line,
    finally:
        hosts.close()


if __name__ == "__main__":
    file_f(filename='/etc/hosts')
    with file('/etc/hosts') as w_f:
        for line in w_f:
            if line.startswith('#'):
                continue
            print line,

