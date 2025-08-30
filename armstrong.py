#153 == 1^3 + 5^3 + 3^3

n = 153
num = n
num1 = 0
nod = len(str(n))  #number of digits

while num > 0:
    digit = num % 10
    num1 += (digit**nod)
    num //= 10

if num1 == n:
    print("armstrong!")
else:
    print("not a armstrong number")    


    ##Time Complexity
    #O(log10n)

    #Space Complexity
    #O(1)