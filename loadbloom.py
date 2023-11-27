#!/usr/bin/env python
# Author Dario Clavijo 2017
# GPlv3

import bloom
import sys
import fileinput

SIZEMB=int(sys.argv[1])
bf = bloom.BloomFilter(array_size=(1024**2)*SIZEMB,do_hashing=False,slice_bits=120,slices=7,ishex=True)

new=0
seen=0
with open(sys.argv[2],'r+') as fp:
    for line in fp:
        try:
            #h=str(int(line.rstrip(),16)).encode('utf8')
            h = line.rstrip()
            #print(h)
        except:
            h=None
        if h != None:
            if bf.update(h)==False:
                new+=1
            else:
                seen+=1
        print("new:%d seen:%d" %(new,seen))

    if new > 0:
        bf.save(sys.argv[3])

