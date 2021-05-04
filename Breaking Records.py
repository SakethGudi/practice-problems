

import math
import os
import random
import re
import sys

def breakingRecords(scores):
    min=scores[0]
    max=scores[0]
    count_m=0
    count_M=0
    for i in scores:
        if(i>max):
            max=i
            count_M=count_M+1
        elif(i<min):
            min=i
            count_m=count_m+1
    return (count_M,count_m)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
