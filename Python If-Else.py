#!/bin/python

import sys


N = int(raw_input().strip())

if N % 2 == 0:
    if N >= 2 and N <= 5:
        print "tidak aneh"
    elif N >= 6 and N <= 20:
        print "aneh"
    elif N > 20:
        print "tidak aneh"
else:
    print "aneh"
