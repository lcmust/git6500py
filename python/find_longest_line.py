#!/usr/bin/env python
#coding=utf-8

import os, sys

def find_longest(file):
    longest = 0
    if not os.path.isfile(file): return
    with open(file, 'r') as f:
        while True:
            line = f.readline()
            if not len(line): break
            linelen = len(line.strip())
            if linelen > longest:
                longest = linelen
    return longest

if __name__ == "__main__":
    print find_longest(sys.argv[1])
