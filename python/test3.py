#!/usr/bin/env python
#coding=utf-8

class BaseBase(object):
    def method(self):
        print "BaseBase"

class Base1(BaseBase):
    pass

class Base2(BaseBase):
    def method(self):
        print 'Base2'

class MyClass(Base1, Base2):
    pass

def func_dict(*arg, **kw):
    if 'name' in kw:
        print kw['name']
    if 'sex' in kw:
        print kw['sex']
    for key in kw:
        print key, '=>', kw[key]
    print type(kw), kw

def fab(max):
	n, a, b = 0, 0, 1
	L = []
	while n < max:
		L.append(b)
		a, b = b, a + b
		n = n + 1
	return L
        
if __name__ == "__main__":
	print "yes, i am main"
