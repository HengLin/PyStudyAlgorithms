#!/usr/bin/env python

from operator import itemgetter
import sys

func_name = None
#func_name = 'appSearchServer'
avg_latency = 0.0
total_count = 0
total_time = 0.0
name = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    name, latency = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        latency = float(latency)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    
    if func_name == name:
        total_count = total_count + 1
       	total_time += latency
    else:
        if func_name:
            print '%s\t%f' % (func_name, total_time)
            print '%s\t%s' % (func_name, total_count)
            print '%s\t%f' % (func_name, total_time / total_count)
        func_name = name
        total_count = 1
        total_time = latency

#avg_latency = total_time / total_count
# do not forget to output the last word if needed!
if func_name == name:
    print '%s\t%f' % (func_name, total_time)
    print '%s\t%s' % (func_name, total_count)
    print '%s\t%f' % (func_name, total_time / total_count)
