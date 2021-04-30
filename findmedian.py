import math
import os
import random
import re
import sys



def findMedian(arr):
    arr.sort()
    n=len(arr)
    m=(n-1)//2
    result=0
    i=0
    for i in range(n):
        if(i==m):
            result=result+arr[i]
        else:
            result=result
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
