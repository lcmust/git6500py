#!/usr/bin/env python
#coding=utf-8

dic1 = {'user': 'username',
        'pwd': 'password'}

class Countdown(object):
    def __init__(self, n):
        self.n = n
    def next(self):
        r = self.n
        self.n += 1
        return r

def make_dict(data):
    resu = {}
    if isinstance(data, dict):
        for tmp in data:
            if tmp == "user" or tmp == "pwd":
                resu[tmp] = data[tmp]
    return resu

def learn_func(*list1, **dict1):
    i = 0
    for tmp in list1:
        print "list1[%d]: %s" %(i, tmp)
        i += 1
    i = 0
    for tmp in dict1:
        print "%d, dict[%s]->%s" %(i, tmp, dict1[tmp])
        i += 1

if __name__ == "__main__":
    # resu = make_dict(dic1)
    # print resu, "type:%s" % type(resu)
    learn_func("list1", "list2", usr = "user1", pwd = "Password1")
    print "OVER"
