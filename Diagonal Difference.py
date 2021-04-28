

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    diagonal1=[]
    diagonal2=[]
    i=0
    j=0
    for i in range(n):
        for j in range(n):
            if(i==j):
                diagonal1.append(arr[i][j])
            else:
                diagonal1=diagonal1
    for i in range(n):
        for j in range(n):
            if(i+j==n-1):
                diagonal2.append(arr[i][j])
            else:
                diagonal2=diagonal2
    x=sum(diagonal1)
    y=sum(diagonal2)
    result=abs(x-y)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
