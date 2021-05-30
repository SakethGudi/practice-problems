import math
import os
import random
import re
import sys


def beautifulBinaryString(b):
    k='010'
    i=0
    count=0
    x=list(b)
    while i<len(b):
        a=x[i:i+3]
        if(''.join(a)==k):
            if(a[2]=='0'):
                x[i+2]='1'
            else:
                x[i+2]='0'
            count=count+1
        i=i+1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
