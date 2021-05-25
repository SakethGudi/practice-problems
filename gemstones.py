import math
import os
import random
import re
import sys

def gemstones(arr):
    a=arr
    while len(a)>1:
        a=[set(a[0]).intersection(set(a[i])) for i in range (len(a)) if(i>0)]
    return len(a[0])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
