

import math
import os
import random
import re
import sys
from itertools import combinations


def birthday(s, d, m):
    number=0
    a=list(s[i:i+m] for i in range(len(s)))
    number=0
    for i in a:
        if(sum(i)==d):
            number=number+1
        else:
            number=number
    return number

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
