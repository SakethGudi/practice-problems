import math
import os
import random
import re
import sys


def icecreamParlor(m, arr):
    i=0
    j=0
    array=[]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(arr[i]+arr[j]==m and i!=j and j>i ):
                a=[i+1,j+1]
                array.append(a)
            else:
                array=array
    return array[0]
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
