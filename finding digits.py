import math
import os
import random
import re
import sys




def findDigits(n):
    arr=list(map(int, str(n)))
    count=0
    i=0
    for i in range(len(arr)):
        if (arr[i]!=0 and n%arr[i]==0):
            count=count+1
        else:
            count=count
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
