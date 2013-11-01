#!/usr/bin/python
#coding=utf-8

print "Hello python"
class Abc():
    num_class = 0
    def __init__(self, msg_tmp=None):
        Abc.num_class += 1
        self.version = "version 0.01"
        # if not msg_tmp:
        #     self.msg = self.version
        # else:
        #     self.msg = msg_tmp
        self.msg = msg_tmp if msg_tmp else None

    def __del__(self):
        Abc.num_class -= 1

    def print_msg(self):
        return self.msg

    def print_num(self):
        print "func:print_num"
        return Abc.num_class

class Abcd(Abc):
    # def __init__(self):
    #     pass
    def print_msg(self):
        print "Abcd class:print_msg"

def countdown(n):
    print "Counting down from %d" % n
    while n > 0:
        yield n
        n -= 1
    return

def receiver():
    print "Ready to receive"
    while True:
        n = (yield)
        print "Got %s" %n

def coroutine(func):
    def start(*args, **kwargs):
        g = func(*args, **kwargs)
        g.next()
        return g
    return start

@coroutine
def receiver():
    print "Ready to receive"
    while True:
        n = (yield)
        print "Got %s" %n




if __name__ == "__main__":
    s11 = Abc("hello python")
    s11.print_msg()
