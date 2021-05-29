import math
import os
import random
import re
import sys

def encryption(s):
    x=int(math.sqrt(len(s)))
    y=x+1
    if(x*x)>=len(s):
        a=[s[i:i+x] for i in range(0,len(s),x)]
    elif(x*y)>=len(s):
        a=[s[i:i+y] for i in range(0,len(s),y)]
        for i in range(len(a)):
            if(len(a[i])<y):
                a[i]=str(a[i])+str('X')*(y-len(a[i]))
    else:
        a=[s[i:i+y] for i in range(0,len(s),y)]
        for i in range(len(a)):
            if(len(a[i])<y):
                a[i]=str(a[i])+str('X')*(y-len(a[i]))
      
    result = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
    [i.remove('X') for i in result if ('X' in i)]
    k=[''.join(i) for i in result]
    return ' '.join(k)
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
