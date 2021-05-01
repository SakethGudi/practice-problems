import math
import os
import random
import re
import sys
def timeConversion(s):
    arr1=list(s.split(":"))
    time=[x for x in arr1[2] if arr1[2].isupper()]
    if(time[2]=='P' and arr1[0]!='12'):
        (arr1[0])=int(arr1[0])+12
    elif(time[2]=='A' and arr1[0]=='12'):
        arr1[0]='00'
    else:
        arr1[0]=arr1[0]
    arr1[0]=str(arr1[0])
    arr1.remove(arr1[2])
    time.remove(time[2])
    time.remove(time[2])
    time=time[0]+time[1]
    arr1.append(time)
    s=":"
    final=s.join(arr1)
    
    return final
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
