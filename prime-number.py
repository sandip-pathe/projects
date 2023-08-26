# this is code to check if the number is prime or not
import sys

def prime(n):
    if n.isdigit():
        n = int(n)
    div = 2
    while div < n:
        if n % div == 0:
            return "NOT Prime Number"
        div += 1
    else:
        return "Prime Number"

number = sys.argv[1]
print(prime(number))
