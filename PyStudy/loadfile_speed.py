#!/usr/bin/env python

import datetime

count = 0
begin_time = datetime.datetime.now()

def readInChunks(fileObj, chunkSize=2048):
    """
    Lazy function to read a file piece by piece.
    Default chunk size: 2kB.
    """
    while True:
        data = fileObj.read(chunkSize)
        if not data:
            break
        yield data

f = open('bigfile')
for chuck in readInChunks(f):
    count = count + 1

end_time = datetime.datetime.now()
total_time = end_time - begin_time

print "chunk=%s, count=%i"%(total_time, count)
f.close()

count = 0
begin_time = datetime.datetime.now()
f = open('bigfile')
for line in f:
    count = count + 1

end_time = datetime.datetime.now()
total_time = end_time - begin_time

print "read=%s, count=%i"%(total_time, count)

f.close()
