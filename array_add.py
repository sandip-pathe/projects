#!/bin/python3

import math
import os
import random
import re
import sys
import array

list = [1,2,3,4]
#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    k = 0
    for element in enumerate(ar):
        k = k + element
    return k


print(simpleArraySum(list))