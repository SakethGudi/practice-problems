import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    a=[x1+i*v1 for i in range(0,10000)]
    b=[x2+i*v2 for i in range(0,10000)]
    result="NO"
    for i in range(len(a)):
        if(a[i]==b[i]):
            result="YES"
            break     
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
