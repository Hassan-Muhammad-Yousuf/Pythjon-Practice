#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    n = len(s)
 
    if s == s[::-1]:
        return -1
    
    for i in range(n):
        if s[i] != s[n-1-i]:
            if s[i+1:n-i] == s[i+1:n-i][::-1]:
                 return i
            elif s[i:n-1-i] == s[i:n-1-i][::-1]:
                 return n-1-i
    return -1
            

if __name__ == '__main__':
    q = int(input().strip())

    for _ in range(q):
        s = input()
        result = palindromeIndex(s)
        print(result)
