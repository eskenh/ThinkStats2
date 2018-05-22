"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function
from collections import defaultdict

import numpy as np
import sys

import nsfg
import thinkstats2

def ReadAndCompare():
    resp = ReadFemResp()
    preg = ReadFemPreg()
    
    pregTimes = defaultdict(list)
    for index, caseid in preg.caseid.iteritems():
        pregTimes[caseid].append(index)

    print(resp.pregnum.value_counts(sort=False))
    
    caseid = 2298
    print(len(pregTimes[caseid]))
    print(resp[resp.caseid == caseid].pregnum.values)
    
    return df

def main(script):
    """Tests the functions in this module.
    
    script: string script name
    """
    ReadAndCompare()
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
