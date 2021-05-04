import math
import os
import random
import re
import sys


def equalizeArray(arr):
    k=sorted(set(arr))
    counts=[]
    for i in range(len(k)):
        counts.append(arr.count(k[i]))
    counts.remove(max(counts))
    return sum(counts)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
