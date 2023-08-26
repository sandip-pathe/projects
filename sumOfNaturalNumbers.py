# This is the code for sum of 1st n natural numbers
import sys

def sum_naturals(n):
    sum = 0
    if n.isdigit():
        n = int(n)
    for number in range(n+1):
        sum += number
    return sum

x = sys.argv[1]
print(sum_naturals(x))