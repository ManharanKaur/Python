#Capitalize
#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the solve function below.
def solve(s):
    result = list(s)
    result[0] = result[0].capitalize()
    for i in range(len(result)):
        if result[i] == ' ' and result[i+1] != ' ':
            result[i+1] = result[i+1].capitalize()
    return "".join(result)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
