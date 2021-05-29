import math
import os
import random
import re
import sys
def timeInWords(h, m):
    dict={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve'}
    dict2={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',
          13:'thirteen',14:'fourteen',15:'quarter',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',21:'twenty one',
          22:'twenty two',23:'twenty three',24:'twenty four',25:'twenty five',26:'twenty six',27:'twenty seven',28:'twenty eight',29:'twenty nine',
          30:'half'}
    if(m==0):
        return str(dict[h])+str(" o'" )+str(' clock')
    elif(1<=m<=30):
        if(int(m)==1):
            return str(dict2[int(m)])+' minute past '+str(dict[h])
        elif(int(m)==30 or int(m)==15):
            return str(dict2[int(m)])+' past '+str(dict[h])
            
        else:
            return str(dict2[int(m)])+' minutes past '+str(dict[h])
    elif(30<m<60):
        if(int(m)==59):
            return str(dict2[60-int(m)])+' minute to '+str(dict[h+1])
        elif(int(m)==45):
            return str(dict2[60-int(m)])+' to '+str(dict[h+1])
        else:
            return str(dict2[60-int(m)])+' minutes to '+str(dict[h+1])

    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
