import math
import os
import random
import re
import sys



def squares(a, b):
    count=0
    c=int(math.sqrt(b))
    a1=[i*i for i in range(c+1)]
    a2=[i for i in a1 if(a<=i<=b)]
    return len(a2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
