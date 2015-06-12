#!/usr/bin/env python

import datetime

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
    """
    nothing to do
    """

end_time = datetime.datetime.now()
total_time = end_time - begin_time

print total_time.seconds
print total_time
