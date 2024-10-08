#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    m = 0
    n = len(q)
    for i in range(n):
        if q[i] - (i + 1) > 2:
            print("Too Chaotic")
            return
       
        for j in range(max(0, q[i]-2), i):
            if q[j] > q[i]:
                m += 1
    print(m)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
