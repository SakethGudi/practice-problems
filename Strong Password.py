import math
import os
import random
import re
import sys
def minimumNumber(n, password):
    a=list('!@#$%^&*()-+')
    count=0
    U=[i for i in password if(i.isupper())]
    if(len(U)==0):
        count=count+1
    L=[i for i in password if(i.islower())]
    if(len(L)==0):
        count=count+1
    D=[i for i in password if(i.isdigit())]
    if(len(D)==0):
        count=count+1
    S=[i for i in password if(i in a)]
    if(len(S)==0):
        count=count+1
    if(count+len(password)>=6):
        return count
    else:
        return 6-len(password)
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
