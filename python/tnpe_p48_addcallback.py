#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.internet.defer import Deferred

def myCallback(result):
    print result

def myErrback(failure):
    print failure

d = Deferred()
## d.addErrback(myErrback)
## d.errback("Triggering errback.")
d.addCallback(myCallback)
d.callback("TRiggering callback.")
