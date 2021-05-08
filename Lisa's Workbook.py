import math
import os
import random
import re
import sys

def workbook(n, k, arr):
    a=[list(range(1,arr[i]+1)) for i in range(len(arr))]
    b=[i[j:j+k] for i in a 
        for j in range(0,len(i),k)]
    count=0
    for i in range(1,len(b)+1):
        if(i in b[i-1]):
            count=count+1
        else:
            count=count
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
