import math
import os
import random
import re
import sys


def funnyString(s):
    a1=[abs(ord(s[i])-ord(s[i-1])) for i in range(1,len(s))]
    b=list(s)
    b.reverse()
    x=''.join(b)
    a2=[abs(ord(b[i])-ord(b[i-1])) for i in range(1,len(s))]
    if(a1==a2):
        return 'Funny'
    else:
        return 'Not Funny'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
