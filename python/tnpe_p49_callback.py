#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.internet.defer import Deferred

def addBold(result):
    return "<b>%s</b>" % (result,)

def addItalic(result):
    return "<i>%s</li>" % (result,)

def printHTML(result):
    print result
    

d = Deferred()
d.addCallback(addBold)
d.addCallback(addItalic)
d.addCallback(printHTML)
d.callback("Hello world.")
