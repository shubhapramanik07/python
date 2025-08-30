from math import *
num = 12563
n = num
#it's a good habit to place variables into another
def count_digits(n):
    return floor(log10(n)) + 1 if n > 0 else 1
#to print
print (count_digits(n))