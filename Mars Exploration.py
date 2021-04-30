
import math
import os
import random
import re
import sys



def marsExploration(s):
    arr=[s[i:i+3] for i in range(0,len(s),3)]
    result=0
    key="SOS"
    for i in arr:
        for j in range(len(key)):
            if(i[j]!=key[j]):
                result=result+1
            else:
                result=result
    return result
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
