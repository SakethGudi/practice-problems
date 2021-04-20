import math
import os
import random
import re
import sys
arr = list(map(int,input().strip().split()))
arr.sort()
arr1=arr
arr2=arr1[0:4]
x=sum(arr2)
arr3=arr1[1:5]
y=sum(arr3)
print(x,y)
