#!/usr/bin/env python
# Author Dario Clavijo 2017
# GPlv3

# used for checking have i been pwnd passwords against a bloomfilter

import bloom
import sys
import hashlib

#bf = bloom.BloomFilter(array_size=(1024**3)*8,do_hashing=True)
bf = bloom.BloomFilter(filename=sys.argv[1],array_size=(1024**2)*512,do_hashing=False,slice_bits=120,slices=7,ishex=True)

print(bf.check(hashlib.sha1(sys.argv[2]).hexdigest()))
