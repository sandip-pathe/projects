import random
import sys

def sandip(x):
    number = random.randint(5,9)
    number = number ** x
    return number

input_xx = sys.argv[1]
if input_xx.isdigit():
    input_xx = int(input_xx)
print(sandip(input_xx))