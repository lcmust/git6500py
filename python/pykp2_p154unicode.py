#!/usr/bin/env python
"""
An example of reading and writing Unicode strings
"""

CODEC='utf-8'
FILE='/tmp/unicode.txt'

hello_out = u"Hello World\n"
bytes_out = hello_out.encode(CODEC)

f = open(FILE, "w")
f.write(bytes_out)
f.close()

f = open(FILE, "r")
bytes_in = f.read()
f.close()
hello_in= bytes_in.decode(CODEC)
print hello_in,

