
import math
import os
import random
import re
import sys

def migratoryBirds(arr):
    c=[]
    type1=arr.count(1)
    c.append(type1)
    type2=arr.count(2)
    c.append(type2)
    type3=arr.count(3)
    c.append(type3)
    type4=arr.count(4)
    c.append(type4)
    type5=arr.count(5)
    c.append(type5)
    x=max(c)
    types=c
    i=0
    k=0
    for i in range(len(types)):
        if(x==types[i]):
            k=k+i+1
            break
        else:
            k=k
    return k
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
