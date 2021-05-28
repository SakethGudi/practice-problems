import math
import os
import random
import re
import sys
def taumBday(b, w, bc, wc, z):
    if(bc==wc):
        return b*bc+w*wc
    result=b*bc+w*wc
    if(wc<bc and wc+z<bc):
        result=(b+w)*wc+b*z
    elif(wc>bc and bc+z<wc):
        result=(b+w)*bc+w*z
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()
