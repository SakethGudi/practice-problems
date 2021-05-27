import math
import os
import random
import re
import sys

def jumpingOnClouds(c):
    x=[index for (index, val) in enumerate(c) if val == 0]
    count=0
    i=min(x)
    while i<max(x):
        if(i+2 in x):
            count=count+1
            i=i+2
        elif(i+1 in x):
            count=count+1
            i=i+1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
