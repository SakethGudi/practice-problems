#!/bin/python3

import math
import os
import random
import re
import sys

def catAndMouse(x, y, z):
    result=str()
    if(abs(x-z)>abs(y-z)):
        result=result+str("Cat B")
    elif(abs(x-z)<abs(y-z)):
        result=result+str("Cat A")
    else:
        result=result+str("Mouse C")
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
