import math
import os
import random
import re
import sys

def jumpingOnClouds(c, k):
    count=100
    n=len(c)
    i=0
    while (True):
        i=(i+k)%n
        if(c[i]==1):
            count=count-3
        elif(c[i]!=1):
            count=count-1
        if(i==0):
            break
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
