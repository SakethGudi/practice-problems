import math
import os
import random
import re
import sys

from itertools import combinations
def maximumPerimeterTriangle(sticks):
    a=list((combinations(sticks,3)))
    out = [item for t in a for item in t]
    subList = [out[n:n+3] for n in range(0, len(out), 3)]
    b=[]
    k=[-1]
    for i in subList:
        if(i[0]+i[1]>i[2] and i[1]+i[2]>i[0] and i[0]+i[2]>i[1]):
            b.append(i)
    sums=[]
    for i in b:
        sums.append(sum(i))
    if(len(sums)>0):
        maxi=max(sums)
    for i in b:
        if(maxi>0 and sum(i)==maxi):
            k=i
            break
        else:
            k=k
        
    return sorted(k)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
