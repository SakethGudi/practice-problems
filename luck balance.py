import math
import os
import random
import re
import sys


def luckBalance(k, contests):
    a=[i[0] for i in contests if(i[1]==1)]
    a.sort()
    if(len(a)>k):
        a1=a[len(a)-k:len(a)]
        a2=a[0:len(a)-k]
        for i in contests:
            if(i[1]==0):
                a1.append(i[0])
    else:
        a1=[i[0] for i in contests]
        a2=[0]
    ans=sum(a1)-sum(a2)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
