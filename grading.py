

import math
import os
import random
import re
import sys



def gradingStudents(grades):
    n=len(grades)
    
    for i in range(len(grades)):
        if (grades[i]>=38) and ((grades[i]%5)>2):
            grades[i]=grades[i]+(5-(grades[i]%5))
        elif (grades[i]>=38) and ((grades[i]%5)<=2):
             grades[i]=grades[i]
        else:
            grades[i]=grades[i]
    return grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
