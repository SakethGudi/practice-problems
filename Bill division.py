

import math
import os
import random
import re
import sys



def bonAppetit(bill, k, b):
    bill.remove(bill[k])
    anna_s=sum(bill)//2
    k=b-anna_s
    if(k>0):
        print(k)
    else:
        print("Bon Appetit")

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
