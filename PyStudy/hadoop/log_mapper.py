#!/usr/bin/env python

import sys
import json

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
	# parse json
    decodejson = json.loads(line)
    
    for event in decodejson["events"]:
        # keys true
		if 'name' in event.keys() and 'ms' in event.keys():		
		    name = event["name"]
		    latency = event["ms"]

		    print '%s\t%f' % (name, latency)
