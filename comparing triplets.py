import math
import os
import random
import re
import sys

a= list(map(int,input().strip().split()))
b= list(map(int,input().strip().split()))
alice=0
bob=0
i=0
for i in range(len(a)):
    if a[i]>b[i]:
        alice+=1
    elif a[i]<b[i]:
        bob+=1
   
print(alice,bob)
