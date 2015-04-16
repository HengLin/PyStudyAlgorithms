#!/usr/bin/env python
import collections

def test():
    print "test"

def count(data, target):
    n = 0
    for v in data:
        if v == target:
            n = n + 1
    return n

if __name__ == '__main__':
    data = [1,2,3,4,3,2,1]
    print count(data,1)
    print count(data,4)
    print count(data,5)

def function():
    pass

class ClassName(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg
        
