#factors_of_10 = [1, 2, 5, 10]
#factors_of_15 = [1, 3, 5, 15]
#factors_of_20 = [1, 2, 4, 5, 10, 20]
#factors_of_25 = [1, 5, 25]
#factors_of_19 = [1, 19]

#######################

# n = 19
# num = n
# factors = []

# for i in range(1,num+1):
#     if num % i == 0:
#         factors.append(i)

# print("factors_of_",n,"=",factors)


#time_complexity: O(n)
#space_complexity: O(k)
#where k is the number of factors of n



#another method to solve the problem.....
from math import sqrt
arr = []
num = 20
for i in range(1, int(sqrt(num)) + 1):
    if num % i == 0:
        arr.append(i)
        if i != (num // i):
            arr.append(num // i)
print("factors_of_", num, "=", sorted(arr))
















