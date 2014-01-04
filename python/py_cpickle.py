#!/usr/bin/env python
#coding=utf-8
import cPickle as p
import sys

shoplistfile = "/tmp/shotlist.data"
shoplist = ['apple', 'mango', 'carrot']
f = file(shoplistfile, 'w')
p.dump(shoplist, f)
f.close()

del shoplist
f = file(shoplistfile)
storedlist = p.load(f)
print storedlist

class test2():
    def __init__(self, name):
        self.name = name

    def __len__(self):
        return len(self.name)

class test1():
    def __init__(self, name):
        self.name = name

    def __len__(self):
        return len(self.name)
    
        
print "Your name:%s" % s
