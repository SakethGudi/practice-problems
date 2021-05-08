import math
import os
import random
import re
import sys

def minimumDistances(a):
    b=[abs(j-i) for i in range(len(a))
              for j in range(len(a))
              if(a[i]==a[j] and i!=j)]
    if(len(b)>0):          
        return min(list(set(b)))
    else:
        return -1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
