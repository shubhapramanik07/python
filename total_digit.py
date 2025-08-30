from math import *
n = 12563
def count_digits(n):
    return floor(log10(n)) + 1 if n > 0 else 1

print (count_digits(n))