import math
import os
import random
import re
import sys

def cavityMap(grid):
    a=[list(i) for i in grid]
    for i in range(len(a)):
        for j in range(len(a)):
            if(i!=0 and j!=0 and i!=len(a)-1 and j!=len(a)-1 and a[i][j]>(a[i-1][j]) and a[i][j]>a[i][j+1] and a[i][j]>a[i][j-1] and a[i][j]>a[i+1][j]):
                a[i][j]=a[i][j].replace(a[i][j],'X')
    b=[''.join(i) for i in a]
    return b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
