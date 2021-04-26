

import math
import os
import random
import re
import sys


def libraryFine(d1, m1, y1, d2, m2, y2):
    a1=[d1,m1,y1]
    a2=[d2,m2,y2]
    fine=0
    if(a1==a2):
        fine=fine
    elif (a1[1]==a2[1] and a1[2]==a2[2] and a1[0]!=a2[0] and d2<d1):
        fine=fine+abs(d2-d1)*15
    elif(a1[1]!=a2[1] and a1[2]==a2[2] and m2<m1):
        fine= fine+ abs(m2-m1)*500
    elif (a2[2]!=a1[2] and y2<y1):
        fine=fine+10000
    else:
        fine=fine
    return fine

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
